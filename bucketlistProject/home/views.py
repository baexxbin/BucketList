from django.shortcuts import render, get_object_or_404, redirect
from .models import Buckets
# from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello, world. You're at the polls home.")
    buckets = Buckets.objects
    return render(request, 'mainpage.html', {'buckets' : buckets})

def signin(request):
    return render(request, 'signin.html')

def login(request):
    return render(request, 'login.html')

def newlist(request):
    return render(request, 'newlist.html')

def mypage(request):
    return render(request, 'mypage.html')