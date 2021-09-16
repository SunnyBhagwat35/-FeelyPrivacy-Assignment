from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db.models import fields
from django.forms.widgets import PasswordInput, TextInput
from .models import User, Schedule

class CreateUserAdminForm(UserCreationForm):
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = '__all__'
        exclude = ['password']

class changeUserAdminForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class appointment(forms.ModelForm):
    time = forms.CharField(widget=TextInput(attrs={'type':'datetime-local'}))
    class Meta:
        model= Schedule
        fields = ['time',]