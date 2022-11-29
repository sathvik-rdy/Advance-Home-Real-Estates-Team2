from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms import modelformset_factory
from django.views.generic import ListView
from .forms import CreateListForm
#ImageForm

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
    listing = Listing.objects.all()
    context = {'listing':listing}
    return render(request,'realtor/listings.html',context)

def realtorlistings(request):
    listing = Listing.objects.all()
    context = {'listing':listing}
    return render(request,'realtor/realtorListings.html',context)

def createListing(request):
    if request.method == "POST":
        prod = Listing()
        prod.propertyName = request.POST.get('Name')
        prod.propertyDescription = request.POST.get('Description')
        prod.propertyNeighborhood = request.POST.get('Neighborhood')
        prod.propertyZipCode = request.POST.get('ZipCode')
        prod.propertyPrice = request.POST.get('propertyPrice')

        if len(request.FILES) != 0:
            prod.propertyImage = request.FILES['propertyImage']
        prod.save()
        messages.success(request, "Listing added successfully")
        return redirect("/")
    return render(request, 'realtor/createListing.html')
def events(request):
    return render(request,'realtor/events.html',{'title':'events'})

def login(request):
    return render(request,'realtor/login.html',{'title':'login'})

def search(request):
    return render(request,'realtor/search.html',{'title':'search'})




#def createProperty(request):

#    form = CreateListForm()
#    if request.method == 'POST':
#        form = CreateListForm(request.POST,request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('/')

#    context = {'form':form}
#    return render(request, 'realtor/property_form.html',context)

#def createProperty(request):

    #ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=4)

    #if request.method == 'POST':
    #    form = CreateListForm(request.POST)
    #    formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())

    #    if form.is_valid() and formset.is_valid():
    #        list_form = form.save()
    #        list_form.save()
    #        for img_form in formset:
    #            if img_form:
    #                image = img_form.cleaned_data['image']
    #                photo = Images(listing=list_form, image=image)
    #                photo.save()
    #        messages.success(request,
    #                         "Yeeew, check it out on the home page!")
    #        return redirect('/')
    #    else:
    #        print(form.errors, formset.errors)
    #else:
    #    form = CreateListForm()
    #    formset = ImageFormSet(queryset=Images.objects.none())
    #context = {'form': form, 'formset': formset}
    #return render(request, 'realtor/property_form.html', context)

def updateProperty(request, pk):

    property = Listing.objects.get(id=pk)
    form = CreateListForm(instance=property)
    if request.method == 'POST':
        form = CreateListForm(request.POST, request.FILES,instance=property)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'realtor/property_form.html', context)

def deleteProperty(request, pk):
    property = Listing.objects.get(id=pk)
    if request.method == 'POST':
        property.delete()
        return redirect('/realtorlistings/')
    context = {'item':property}
    return render(request, 'realtor/delete_property.html', context)