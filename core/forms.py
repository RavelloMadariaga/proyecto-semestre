from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='Correo')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        help_texts = {k:"" for k in fields } 

class EditProfileForm(UserChangeForm):

    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='Correo')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password = None
    
    class Meta:
        model = User
        fields = ['username',
        'email',
        'first_name',
        'last_name']