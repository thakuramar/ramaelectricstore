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
from .views import Index, About, Sales, Service, Pricing, Detail, Feedback,  contact, \
    DetailView, TestCreate, FormAppointmentFormView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about.html', About.as_view(), name='about'),
    path('service.html', Service.as_view(), name='service'),
    path('pricing.html', Pricing.as_view(), name='pricing'),
    path('sales.html', Sales.as_view(), name='sales'),
    path('feedback.html', Feedback.as_view(), name='feedback'),
    path('f-detail.html', Detail.as_view(), name='f-detail'),

    path('detail_list.html', DetailView.as_view(), name='detail'),
    path('test_create.html', TestCreate.as_view(), name='create'),
    path('appointment.html', FormAppointmentFormView.as_view(), name='appointment'),

    path('contact.html', views.contact, name='contact'),












]
