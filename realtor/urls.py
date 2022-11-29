from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.homeListView.as_view(), name='realtor-home'),
    path('about/', views.aboutListView.as_view(), name='realtor-about'),
    path('listings/', views.listings, name='listings'),
    path('realtorlistings/', views.realtorlistings, name='realtor-listings'),
    path('events/', views.events, name='realtor-events'),
    path('search/', views.search, name='realtor-search'),
    path('createListing/', views.createListing, name='realtor-createListing'),
   # path('create_property/', views.createProperty, name='realtor-create_property'),
    path('update_property/<str:pk>/', views.updateProperty, name='realtor-update-property'),
    path('delete_property/<str:pk>/', views.deleteProperty, name='realtor-delete-property')
]
