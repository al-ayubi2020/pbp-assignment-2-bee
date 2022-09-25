from django import forms

class CreateForm(forms.Form):
    title = forms.TextInput(label='Title')
    description = forms.Textarea(label='Description')