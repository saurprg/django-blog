from django import forms
from django.forms import widgets
class LoginForm(forms.Form):
    title = forms.CharField(widget = forms.TextInput(
        attrs ={
            'class' : 'title',
            'name' : 'title',
            'placeholder' : 'Enter title'
        }
    ),required=True)
    txt = forms.CharField(widget = forms.Textarea(
        attrs= {
            'name' : 'txt',
            'placeholder' : 'Write your Post Here'
        }
    ),required=True)


