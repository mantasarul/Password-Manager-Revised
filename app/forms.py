from django.forms import widgets
from .models import Account, Mail, Phone
from django import forms

class AccountForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = ['category', 'url', 'username', 'password', 'mail_id', 'phone_id', 'recovery_code']
        labels = {
            'category': 'Category',
            'url': 'URL',
            'username': 'Username',
            'password': 'Password',
            'mail_id': 'Email',
            'phone_id': 'Phone',
            'recovery_code': 'Recovery Code'

        }
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Category'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'mail_id': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Email Address'}),
            'phone_id': forms.Select(attrs={'class': 'form-control'}),
            'recovery_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter comma seperated Recovery Codes. Example: 123456, 789456'}),

        }


class MailForm(forms.ModelForm):

    class Meta:
        model = Mail
        fields = ['mail']
        labels = {
            'mail': 'Mail'
        }
        widgets = {
            'mail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mail'}),
        }


class PhoneForm(forms.ModelForm):

    class Meta:
        model = Phone
        fields = ['phone']
        labels = {
            'phone': 'Phone'
        }
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone'}),
        }
