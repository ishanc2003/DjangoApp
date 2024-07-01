from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page! Ishan Try http://20.244.45.96:8000/print/")

def print_message(request):
    return HttpResponse("LTIMindtree Ishan Microsoft Azure Github CI/CD Pipeline ")

