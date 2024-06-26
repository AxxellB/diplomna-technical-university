from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
        }
        help_texts = {
            'username': '',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required!')
        return email
