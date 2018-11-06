from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username' ,'email' ,'password1' ,'password2']

class UserUpdateForm(ModelForm):
    email = forms.EmailField()
    class Meta:
        fields = ['username','email']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']