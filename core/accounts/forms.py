from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    """
    Attributes added to customise for bootstrap
    """
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "name": "first_name",
                "placeholder": "First Name"
            }),
        label="First Name"
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "name": "last_name",
                "placeholder": "Last Name"
            }),
        label="Last Name"
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "email",
                "name": "email",
                "placeholder": "Email"
            }),
        label="Email"
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "name": "password1",
                "placeholder": "Password"
            }
        ),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "name": "password2",
                "placeholder": "Confirm Password"
            }
        ),
        label="Confirm Password"
    )
    university = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "name": "university",
                "placeholder": "University"
            }
        ),
        label="University"
    )
    degree_commencement_year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "name": "degree_commencement_year",
                "placeholder": "Pharmacy Degree Commencement Year"
            }
        ),
        label="Degree Commencement Year"
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "university",
            "degree_commencement_year"
        ]
class LoginForm(forms.Form):
    '''Attributes added to customise for bootstrap'''
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type':'text', 'name': 'Email', 
            'placeholder': 'Email'}), label="Email")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'type':'password', 'name':'password1', 
            'placeholder': 'Password'}), label="Password")

    error_messages = {
        'invalid_login': ("Please enter a correct %(email)s and password. "
                           "Note that both fields may be case-sensitive."),
        'inactive': ("This account is inactive."),
    }