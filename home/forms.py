from django.forms import ModelForm, TextInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



class SignUpForm(UserCreationForm):
  #extend the email field from the stock UserCreationForm
  email = forms.EmailField(label="Email Address", required=True)

  class Meta:
    model=User
    fields=( "username", "email", "password1", "password2")

  #Override the __init__ method so that the form fields line up
  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['email'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'

    
  #example of how to custom clean with own error msg.
  def clean_username(self):
    username = self.cleaned_data['username'].lower()
    r = User.objects.filter(username=username)
    if r.count():
        raise  ValidationError("Username already exists")
    return username



