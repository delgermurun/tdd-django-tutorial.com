from django.views.generic import ListView, FormView

from .models import Poll
from .forms import PollVoteForm


class Base(object):
    model = Poll


class Home(Base, ListView):
    context_object_name = 'polls'


class Detail(Base, FormView):
    form_class = PollVoteForm
    template_name = 'polls/poll_detail.html'

    def get_form_kwargs(self, **kwargs):
        kwargs = super(Detail, self).get_form_kwargs(**kwargs)
        kwargs['poll'] = Poll.objects.get(pk=self.kwargs['pk'])
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs = super(Detail, self).get_context_data(**kwargs)
        kwargs['poll'] = Poll.objects.get(pk=self.kwargs['pk'])
        return kwargs
