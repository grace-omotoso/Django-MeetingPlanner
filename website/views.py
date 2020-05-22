from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting, Room
# Create your views here.
def welcome(request):
    #return HttpResponse("Welcome to Meeting Planner")
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at " +str(datetime.now()))

def about(request):
    return  HttpResponse("My name is Grace and I am learning Django")