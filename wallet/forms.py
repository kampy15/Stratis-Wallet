from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registerform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter username'}))
    LastName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter LastName'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control my-2','placeholder':'Enter Email'}))
    password1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Password'}))
    password2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username','LastName','email','password1','password2']