from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hyderabad(request):
    return render(request,"hyderabad.html")
def warangal(request):
    response = "<h1>Welcome to Warangal</h1>"
    return HttpResponse(response)