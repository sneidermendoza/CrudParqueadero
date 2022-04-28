from django import forms
from django.contrib.auth.models import User

class RegistroFormulario(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id' : 'username',
                                    'placeholder': 'Nombre completo '
                                }))
    email = forms.EmailField(required=True,
                                widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'id' : 'email',
                                    'placeholder': 'Ejemplo@sms.com'
                                }))
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                }))
    password2= forms.CharField(label='Confirmar password',required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                }))

    def clean_username(self): # obligatorio el clean_ para que django lo reconozca como una validacion
        username = self.cleaned_data.get('username') # para traerse el username que ingresa el usuario

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Nombre de usuario ya se encuentra en uso')
        
        return username

    def clean_email(self): # obligatorio el clean_ para que django lo reconozca como una validacion
        email = self.cleaned_data.get('email') # para traerse el email que ingresa el usuario

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El imeil ya se encuentra en usu')
        
        return email

    def clean(self): # se sobrescribe este metodo para validar las dos contraseñas
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'El password no coiciden')

    def save(self):
        return User.objects.create_user(
                self.cleaned_data.get('username'),
                self.cleaned_data.get('email'),
                self.cleaned_data.get('password')
            )
