from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def finance(request):
    return HttpResponse("Finance Module")