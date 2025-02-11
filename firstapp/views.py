from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to my first Django app!")

def main(request):
    return HttpResponse("Welcome")    

def sample(request):
    return HttpResponse("Hello, Sample")

def function(request):
    return HttpResponse('Hello, function old')

    