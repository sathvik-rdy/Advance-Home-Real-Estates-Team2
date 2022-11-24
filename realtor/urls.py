from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.homeListView.as_view(), name='realtor-home'),
    path('about/', views.about, name='realtor-about'),
    path('listings/', views.listings, name='realtor-listings'),
    path('events/', views.events, name='realtor-events'),
    path('search/', views.search, name='realtor-search'),
]
