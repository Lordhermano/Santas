from django import forms

class Register(forms.Form):
    account_type = (
        (1, 'Standard'),
        (2, 'Premium'),
        (3, 'VIP')
    )
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=400)
    account = forms.ChoiceField(choices=account_type)
    password = forms.CharField(max_length=200)