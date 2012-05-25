from django.views.generic import ListView, FormView
from django.core.urlresolvers import reverse

from .models import Poll
from .forms import PollVoteForm


class Base(object):
    model = Poll


class Home(Base, ListView):
    context_object_name = 'polls'


class Detail(Base, FormView):
    form_class = PollVoteForm
    template_name = 'polls/poll_detail.html'
    object = None

    def get_success_url(self):
        return reverse('polls-detail', args=[self.object.pk])

    def form_valid(self, form):
        form.add_vote()
        return FormView.form_valid(self, form)

    def get_object(self):
        if self.object is None:
            self.object = Poll.objects.get(pk=self.kwargs['pk'])
        return self.object

    def get_form_kwargs(self, **kwargs):
        kwargs = super(Detail, self).get_form_kwargs(**kwargs)
        kwargs['poll'] = self.get_object()
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs = super(Detail, self).get_context_data(**kwargs)
        kwargs['poll'] = self.get_object()
        return kwargs
