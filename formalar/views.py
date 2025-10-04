from django.shortcuts import render, redirect

# Create your views here.

from .models import Savollar
from .forms import SavollarForm

def home(request):
    return render(request,'thank_you.html')

def savollar(request):
    if request.method == 'POST':
        form = SavollarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = SavollarForm()

    return render(request,'forma.html',{'form':form})




