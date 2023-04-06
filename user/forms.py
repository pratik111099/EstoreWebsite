from django.forms import ModelForm, TextInput, EmailInput, NumberInput, PasswordInput
from .models import User
from django.contrib.auth.forms import UserCreationForm

class loginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','password']
        # fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),

            'password': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
                }),
        }


class registrationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'email', 'mobile_number' , 'password1', 'password2']
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),

            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                }),

            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),

            'mobile_number': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Mobile Number'
                }),
           
        }