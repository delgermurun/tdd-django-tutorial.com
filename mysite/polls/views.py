from django.views.generic import ListView, DetailView

from .models import Poll


class Base(object):
    model = Poll


class Home(Base, ListView):
    context_object_name = 'polls'


class Detail(Base, DetailView):
    pass
