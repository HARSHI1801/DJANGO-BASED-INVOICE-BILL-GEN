from django import forms
from .models import Snippet


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-mail')
    category = forms.ChoiceField(choices=[('option', 'Option'), ('other', 'Other'), ('question 1', 'Question 1')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name', 'body')
