from django.shortcuts import render, get_object_or_404, redirect
from .models import Buckets
from django.http import HttpResponse

# Create your views here.
def addlist(request):
    return HttpResponse("addlist page")
    # buckets = Buckets.objects
    # return render(request, 'addlist.html')