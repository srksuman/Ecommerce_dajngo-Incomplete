from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import ProductEntry


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(
        label='Re-Enter-password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'email': 'Email'
        }


class ProductEntryForm(forms.ModelForm):
    
    class Meta:
        model = ProductEntry
        fields = ['image', 'productname', 'price', 'productdesc']
        labels = {'image': 'Product Image',
                  'productname': 'Product Name',
                  'productdesc': 'Product Description',
                  }
