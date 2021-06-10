from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields

from app_login.models import *



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', )
        
