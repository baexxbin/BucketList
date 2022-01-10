from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Buckets

# Create your views here.
def mypage(request):
    return render(request, 'mypage.html')