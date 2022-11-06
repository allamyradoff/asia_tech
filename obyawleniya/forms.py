from django import forms
from .models import *
from django.forms.widgets import Select


class AdForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Напишите телефон',
        'class': 'form-control'
    }))

    desc = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Напишите фамилаю',
        'class': 'form-control'
    }))

    # cat_id = forms.BooleanField(widget=forms.SelectMultiple(attrs={
    #     'class': 'form-control'
    # }))

    


    


    class Meta:
        model = Ad
        fields = ('name', 'desc', 'image', 'cat_id', 'exchange', 'credit')
        widgets = {
          'cat_id': Select(attrs={'class': 'form-control'}),
        }