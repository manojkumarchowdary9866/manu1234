from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display2(request):
    return HttpResponse('<marquee><h2> display2 the web page<marquee></h2>')
