from django.conf.global_settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .models import Test, AppointmentForm
from .forms import TestForm, FormAppointmentForm, ContactPageForm


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class Sales(View):
    def get(self, request):
        return render(request, 'sales.html')


class Service(View):
    def get(self, request):
        return render(request, 'service.html')


class Pricing(View):
    def get(self, request):
        return render(request, 'pricing.html')


class Detail(View):
    def get(self, request):
        return render(request, 'f-detail.html')


class Feedback(View):
    def get(self, request):
        return render(request, 'feedback.html')


def contact(request):            # getting contactPage data and sending  direct message to the email.
    if request.method == 'GET':
        form = ContactPageForm()
    else:
        form = ContactPageForm(request.POST)
        if form.is_valid():
            message_name = form.cleaned_data['name']
            message_phone = form.cleaned_data['phone']
            message_email = form.cleaned_data['email']
            message_body = form.cleaned_data['message']

            appointment = ' Sender name:__' + message_name + '    Phone:__' + message_phone + '    email:__'\
                          + message_email + '     Message:__' + message_body

            send_mail(
                 'From ' + message_name,  # subject
                 appointment,

                 'Email From' + message_email,  # from sender email
                 [EMAIL_HOST_USER, message_email],  # to my email
                 fail_silently=False,

             )
        return render(request, 'contact.html', {'form': form, 'message_name': message_name})
    return render(request, 'contact.html', {'form': form})




class DetailView(View):
    def get(self, request, *args, **kwargs):
        detailobj = Test.objects.all()

        context = {
            'detailobj': detailobj
        }
        return render(request, 'ramaelectric/detail_list.html',  context)


class TestCreate(View):
    def post(self, request, *args, **kwargs):
        form = TestForm(request.POST or None)
        if form.is_valid():
            form.save()

        context = {
            'form': form
        }
        return render(request, 'ramaelectric/test_create.html',  context)


class FormAppointmentFormView(View):   # appointment section form data rendering and save to database
    def get(self, request, *args, **kwargs):
        form = FormAppointmentForm()
        context = {'form': form}
        return render(request, 'appointment.html', context)

    def post(self, request, *args, **kwargs):
        form = FormAppointmentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'appointment.html', {'form': form})







