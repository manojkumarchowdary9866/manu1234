
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return HttpResponse('<marquee><h1> display the web page<marquee></h1>')
