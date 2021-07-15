from django.shortcuts import render
import datetime
from django.http import HttpResponse

def my_app(request):
    d = datetime.datetime.now()
    s="<h1> the current time is "+str(d)+"</h1>" 
    return HttpResponse(s)

def first(request):
    return HttpResponse("<h1> First </h1>")

def second(request):
    return HttpResponse("<h1> Second </h1>")

def third(request):
    return HttpResponse("<h1> Third </h1>")

def fourth(request):
    return HttpResponse("<h1> Fourth </h1>")