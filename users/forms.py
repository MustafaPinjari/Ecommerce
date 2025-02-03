# users/forms.py
from django import forms
from .models import CustomUser  # Import CustomUser model
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser  # Use the CustomUser model here
        fields = ['username', 'email', 'phone', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
