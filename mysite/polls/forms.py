from django import forms


class PollVoteForm(forms.Form):
    vote = forms.ChoiceField(widget=forms.RadioSelect())

    def __init__(self, poll, initial):
        forms.Form.__init__(self, initial)
        self.fields['vote'].choices = [(c.pk, c.choice) for c in poll.choice_set.all()]
