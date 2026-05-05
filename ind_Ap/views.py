from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chittor(request):
    response = "<h1>Welcome to chittor</h1>"
    return HttpResponse(response)
def kadapa(request):
    response = "<h1>Welcome to Kadapa</h1>"
    return HttpResponse(response)