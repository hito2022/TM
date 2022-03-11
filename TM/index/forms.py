from django import forms
from django.core import validators

class studentForm(forms.Form):
    name = forms.CharField(max_length=10)
    course = forms.ChoiceField(choices=(
        ("read", "read"),
        ("write","write"),
        ("speak","speak"),
        ("listen", "listen")),
        widget=forms.RadioSelect
        )
