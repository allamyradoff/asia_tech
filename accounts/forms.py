from dataclasses import field
from django import forms

from .models import *


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Paroly giriziň',
        'class': 'form-control'
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Paroly tassyklaň',
        'class': 'form-control'

    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Adynyň',
        'class': 'form-control'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Familiýaňyz',
        'class': 'form-control'
    }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Telefon belgiňiz',
        'class': 'form-control'
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email poçtaňyz',
        'class': 'form-control'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name',
            'phone_number', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Iki parolam dogry giriziň")


class UserForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Adyňyz',
        'class': 'form-control'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Fimiliýaňyz',
        'class': 'form-control'
    }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Telefon belgiňiz',
        'class': 'form-control'
    }))

    class Meta:
        model=Account
        fields =['first_name', 'last_name', 'phone_number']


class UserProfileForm(forms.ModelForm):


    address_line_1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Adyňyz',
        'class': 'form-control'
    }))

    address_line_2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Fimiliýaňyz',
        'class': 'form-control'
    }))

    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Telefon belgiňiz',
        'class': 'form-control'
    }))

    state = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Welaýatyňyz',
        'class': 'form-control'
    }))

    profile_avatar = forms.ImageField(required=False, error_messages= {'invalid':("image file only")}, widget=forms.FileInput)


    class Meta:
        model=UserProfile
        fields=('address_line_1', 'address_line_2',
                'city', 'state', 'profile_avatar')
