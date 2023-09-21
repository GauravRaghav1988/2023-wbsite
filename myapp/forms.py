from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from .models import *

class SignUpForm(UserCreationForm):
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'email': 'Email'}



class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"










