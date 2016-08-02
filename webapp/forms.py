from django import forms
from django.contrib.auth.models import User

from webapp.models import Picture


class PictureCreateForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields=['name','pic']
        exclude=('tour',)


class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model=User
        fields=['username','email','password']

