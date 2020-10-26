"""ramaelectricstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import Index, About, Sales, Service, Eservice, Resi, Comm, Contactor, Plumb, Solar,  contact, \
    ItemListView, ItemDetailView, FormAppointmentFormView


#app_name = 'ramaelectric'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about.html', About.as_view(), name='about'),
    path('service.html', Service.as_view(), name='service'),
    path('sales.html', Sales.as_view(), name='sales'),


    path('eservice.html', Eservice.as_view(), name='eservice'),
    path('resi.html', Resi.as_view(), name='resi'),
    path('comm.html', Comm.as_view(), name='comm'),
    path('contractor.html', Contactor.as_view(), name='contractor'),
    path('solar.html', Solar.as_view(), name='solar'),
    path('plumb.html', Plumb.as_view(), name='plumb'),




    path('items_list.html',  ItemListView.as_view(), name='list'),
    path('ramaelectric/<int:pk>',  ItemDetailView.as_view(), name='detail'),
    # path('test_create.html', ItemsCreate.as_view(), name='create'),
    path('appointment.html', FormAppointmentFormView.as_view(), name='appointment'),

    path('contact.html', views.contact, name='contact'),














]
