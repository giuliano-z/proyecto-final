from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioDeCreacionDeUsuarios(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class FormularioEditarUsuario(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre',max_length=50)
    last_name = forms.CharField(label='Apellido',max_length=50)
    avatar = forms.ImageField(required=False)
    bibliografia = forms.CharField(label='Bibliografía', widget=forms.Textarea, required=False)

    class Meta:
        model= User
        fields = ['email', 'first_name', 'last_name', 'avatar', 'bibliografia']