from django.shortcuts import render,redirect
# for logging in and out
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Register,Login,Bookings
from .models import Createaccount,Destination
# Create your views here.

def home(request):
   return render(request, 'page/base.html')



def register(request):
   form = Register()
   if request.method == 'POST':
      form = Register(data=request.POST)
      if form.is_valid():
         form.save()
         name = request.POST.get('name')
         messages.success(request,f"Account created for {name}")
         context = {'form':form}      
         return redirect('login')
      else:
            # If form is invalid, re-render the form with errors
            return render(request, "register.html", {"form": form})
   else:
      context = {'form':Register()}      
      return render(request,'page/register.html',context=context)
   
def login_page(request):
   if request.method == 'POST':
      form = Login(request,data=request.POST)
      if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password )
            print(user)
            if user is not None:
               login(request,user)  
               return redirect('home')
            else:
              messages.info(request,'Username or Password is incorrect')
              context = {'form':Login()}
              return render(request,'page/login.html',context)    

      else:  
         messages.info(request,'Username or Password is incorrect')
         context = {'form':Login()}
         return render(request,'page/login.html',context)    
   else:      
      context = {'form':Login()}
      return render(request,'page/login.html',context)         
def logout(request):
      auth.logout(request)
      return redirect('login')

def display_cards(request):
      dests = Destination.objects.all()

      return render(request,'page/poker.html',{'dest1':dests})
 

@login_required(login_url='login')
def book(request):
    context = {'form':Bookings()}
    return render(request,'page/bookings.html',context)
