from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}),
        error_messages={}
    )
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}),
        error_messages={}
    )
    surname = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}),
        error_messages={}
    )
    password1 = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}),
        error_messages={}
    )
    password2 = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}),
        error_messages={}
    )

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username=username).count():
            raise ValidationError('user already exists')
        return username

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError('password does not match')
        return self.cleaned_data['password2']
