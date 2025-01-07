from django.shortcuts import render

from .forms import Register
# Create your views here.
def home(request):
   return render(request, 'base.html')

def register(request):
   context = {'form':Register()}
   return render(request,'register.html',context=context)