from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import Material
from django.contrib.auth.forms import AuthenticationForm

class MeuFormularioDeLogin(AuthenticationForm):
    pass





class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'  # ou especifique os campos que deseja no formulário