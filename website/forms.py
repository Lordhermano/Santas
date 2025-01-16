from django import forms
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Createaccount

class Register(UserCreationForm):
    class Meta:
        model = Createaccount
        fields = ['name','email','password1','password2','date_of_birth','account']
        widgets = {'account': forms.RadioSelect(),'date_of_birth':forms.DateInput(attrs={'type':'date','max':datetime.now().date()})

        }

class Login(AuthenticationForm): 
    username =  forms.CharField(widget=forms.TextInput())
    password =  forms.CharField(widget=forms.PasswordInput())
        

class Bookings(forms.Form):

    adult = forms.IntegerField(min_value=0)
    childern = forms.IntegerField(min_value=0)
    infants = forms.IntegerField(min_value=0)

