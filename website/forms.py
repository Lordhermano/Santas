from django import forms
from datetime import datetime
from django.contrib.auth.models import User

class Register(forms.Form):
    account_type= (
        (1, 'Standard'),
        (2, 'Premium'),
        (3, 'VIP'),
    )

    name = forms.CharField(max_length=200, label="Full Name")
    email = forms.EmailField(max_length=400, label="Email Address")
    account = forms.ChoiceField(choices=account_type, widget=forms.RadioSelect(), label="Account Type")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter a strong password'}),
        max_length=200,
        label="Password"
    )
    # the placeholder adds astethic feel to the feilds and makes the form much more user friendly
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter your password'}),
        max_length=200,
        label="Confirm Password"
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'max': datetime.now().strftime('%Y-%m-%d')}),
        label="Date of Birth"
    )
    # Authentication
    def clean(self):
        cleaned_data = super().clean()
        passwords = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        

        if passwords != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")


class Login(forms.Form):
    email = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200,widget=forms.PasswordInput)