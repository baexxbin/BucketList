from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the polls home.")
