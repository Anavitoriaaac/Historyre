from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

from django.contrib.auth.forms import AuthenticationForm

class MeuFormularioDeLogin(AuthenticationForm):
    pass
