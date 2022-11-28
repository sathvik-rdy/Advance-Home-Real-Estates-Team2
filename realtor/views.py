from django.shortcuts import render
from django.views.generic import ListView

import users.models
from .models import *
from users.models import *


# Create your views here.
class homeListView(ListView):
    model = Profile
    template_name = 'realtor/home.html'

#def about(request):
#    return render(request,'realtor/about.html',{'title':'about'})
class aboutListView(ListView):
    model = Profile
    template_name = 'realtor/about.html'

def listings(request):
    return render(request,'realtor/listings.html',{'title':'listings'})

def events(request):
    return render(request,'realtor/events.html',{'title':'events'})

def login(request):
    return render(request,'realtor/login.html',{'title':'login'})

def search(request):
    return render(request,'realtor/search.html',{'title':'search'})

