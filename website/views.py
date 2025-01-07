from django.shortcuts import render,redirect

from .forms import Register
from .models import Createaccount
# Create your views here.
def home(request):
   return render(request, 'base.html')

def register(request):
   
   if request.method == 'POST':
      form = Register(request.POST)
      if form.is_valid():
         name = request.POST.get('name','')
         email = request.POST.get('email','')

         # account = request.POST.get('Account','')
         accountchoice = request.POST.get('account','')
         print(accountchoice)
         account = dict(Register.account_type).get(int(accountchoice))
         print(account)
         
         password = request.POST.get('password','')
         date_of_birth = request.POST.get('date_of_birth','')
         acc_obj = Createaccount(name=name,email=email,account=account,password=password,date_of_birth=date_of_birth)
         acc_obj.save()
         context = {'form':form}      
         return render(request,'register.html',context=context)
   else:
      context = {'form':Register()}      
      return render(request,'register.html',context=context)