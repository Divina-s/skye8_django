from django import views
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Skye8 Internship: Django')
def home(request):
    return render(request,'home.html', {})
