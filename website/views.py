from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import Register,Login
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
         account = dict(Register.account_type).get(int(accountchoice))
         password = request.POST.get('password','')
         date_of_birth = request.POST.get('date_of_birth','')
         acc_obj = Createaccount(name=name,email=email,account=account,password=password,date_of_birth=date_of_birth)
         acc_obj.save()
         messages.success(request,f"Account created for {name}")
         context = {'form':form}      
         return redirect('login')
      else:
            # If form is invalid, re-render the form with errors
            return render(request, "register.html", {"form": form})
   else:
      context = {'form':Register()}      
      return render(request,'register.html',context=context)
   

def login(request):
   context = {'form':Login()}
   return render(request,'login.html',context=context)