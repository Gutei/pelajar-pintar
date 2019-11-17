from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from panel.models import School, SchoolContact, AbstractSchool
from django.contrib.admin import widgets


class UserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'style': 'border-bottom:1px solid gray;'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'style': 'border-bottom:1px solid gray;'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'style': 'border-bottom:1px solid gray;'}))
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput(attrs={'style': 'border-bottom:1px solid gray;'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", ]


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = [
            "school_number", "name", "level", "province", "city",
            "address", "logo", "image", "level", "type"
        ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = SchoolContact
        fields = [
            "phone", "email"
        ]
