from django.forms import ModelForm
from .models import User

class loginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','password']
        # fields = '__all__'


class registrationForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'