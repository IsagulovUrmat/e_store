from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['products','quantity','user', 'payment_method' ]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100,help_text='Required')

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
