from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registerform(UserCreationForm):
    firstname = forms.CharField(widget=forms.TextInput)
    username = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password1=forms.CharField(widget=forms.TextInput)
    password2=forms.CharField(widget=forms.TextInput)
    class Meta:
        model = User
        fields = ['username','last_name','email','password1','password2']