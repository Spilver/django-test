from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'hello.html',{'name': 'Esteban'})

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')