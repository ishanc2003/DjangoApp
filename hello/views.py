from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def print_message(request):
    return HttpResponse("LTIMindtree-Ishan")

