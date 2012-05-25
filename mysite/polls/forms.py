from django import forms

from .models import Choice


class PollVoteForm(forms.Form):
    vote = forms.ChoiceField(widget=forms.RadioSelect())

    def __init__(self, poll, **kwargs):
        forms.Form.__init__(self, **kwargs)
        self.fields['vote'].choices = [(c.pk, c.choice) for c in poll.choice_set.all()]
    
    def add_vote(self):
        choice = Choice.objects.get(pk=self.cleaned_data['vote'])
        choice.votes += 1
        choice.save()
