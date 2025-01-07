from django import forms
from datetime import datetime

class Register(forms.Form):
    account_type = (
        (1, 'Standard'),
        (2, 'Premium'),
        (3, 'VIP')
    )
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=400)
    account = forms.ChoiceField(choices=account_type, widget=forms.RadioSelect())
    password = forms.CharField(max_length=200)
    # calendar (IMPORTANT)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'max': datetime.now().date()}))