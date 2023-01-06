from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm

User = get_user_model()

class UsernamePasswordResetForm(PasswordResetForm):
    username = forms.CharField(label='Username')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('There is no user with that username.')
        return username
