from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def homepage(request):  
    template = loader.get_template("starterHTML.html")
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template("register.html")
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())

def chat(request):
    template = loader.get_template("chat.html")
    return HttpResponse(template.render())


