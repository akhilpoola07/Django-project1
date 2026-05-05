from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chittor(request):
    user_name = "Akhil"
    age = 21
    context = { 
        "name":user_name,
        "age": age
        }
    return render(request,"chittor.html",context)
    
def kadapa(request):
    response = "<h1>Welcome to Kadapa</h1>"
    return HttpResponse(response)

def ind(request):
    user_name = "Akhil"
    age = 21
    context = { 
        "name":user_name,
        "age": age
        }
    return render(request,"ind.html",context)
