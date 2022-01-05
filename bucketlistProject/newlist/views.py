from django.shortcuts import render, get_object_or_404, redirect
from .models import Buckets
from django.http import HttpResponse

# Create your views here.
def newlist(request):
    # return HttpResponse("newlist page")
    # buckets = Buckets.objects
    return render(request, 'newlist.html')