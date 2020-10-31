from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required',widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    username = forms.CharField(max_length=200, help_text='Required',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    USER_ACCOUNT_TYPE = (
        ("professional", "Professional"),
        ("client", "Client"),
        )
    account_type = forms.ChoiceField(required=True, choices = USER_ACCOUNT_TYPE)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'account_type')
