from django import forms
from django.contrib.auth import password_validation


class CreateUserForm(forms.Form):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    login = forms.CharField(
        min_length=5,
        max_length=20,
        label='Login:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(
        min_length=4,
        label="Password:",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    password2 = forms.CharField(
        min_length=6,
        label="Password confirmation:",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


class LoginUserForm(forms.Form):
    login = forms.CharField(
        min_length=5,
        max_length=20,
        label='Login:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(
        min_length=4,
        label="Password:",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )