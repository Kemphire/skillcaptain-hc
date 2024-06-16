from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def clean_password2(self):
        password: str = super().clean_password2()
        if len(password) < 8:
            raise ValidationError("password must be atleast 8 charecter's long")
        if not re.search(r"\d", password):
            raise ValidationError("Password must contain at least one digit.")
        if not re.search(r"[A-Za-z]", password):
            raise ValidationError("Password must contain at least one letter.")
        if re.search(r"[^A-Za-z0-9]", password):
            raise ValidationError("Password must not contain special characters.")
        return password

    def clean_username(self) -> str:
        username = super().clean_username()
        if re.search(r"[^A-Za-z0-9]", username):
            raise ValidationError("Username must not contain special characters.")
        return username


class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
