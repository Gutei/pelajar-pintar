from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", ]
