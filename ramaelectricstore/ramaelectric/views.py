from django.conf.global_settings import EMAIL_HOST_USER
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic import FormView
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .models import Items, AppointmentForm
from .forms import ItemsForm, FormAppointmentForm, ContactPageForm


class Index(View):                                # main menu start
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


class Eservice(View):    # service section here
    def get(self, request):
        return render(request, 'eservice.html')


class Resi(View):
    def get(self, request):
        return render(request, 'resi.html')


class Comm(View):
    def get(self, request):
        return render(request, 'comm.html')


class Contactor(View):
    def get(self, request):
        return render(request, 'contractor.html')


class Solar(View):
    def get(self, request):
        return render(request, 'solar.html')


class Plumb(View):
    def get(self, request):
        return render(request, 'plumb.html')


class Career(View):
    def get(self, request):
        return render(request, 'career.html')


def contact(request):            # getting contactPage form data and sending  direct message to the company email and the same email response back to the sender email.

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


class ItemListView(ListView):
    template_name = 'ramaelectric/items_list.html'  # url will be look like this <appname>/<modelname>_list.html
    model = Items


class ItemDetailView(DetailView):
    template_name = 'ramaelectric/items_detail.html'  # url will be look like this <appname>/<modelname>_Detail.html
    model = Items

    # def get_object(self):     # override context data
    #     d_ = self.kwargs.get("pk")
    #     return get_object_or_404(Items, id=d_)
    #

# class ItemsDetail(View):
#     def post(self, request, *args, **kwargs):
#         form = ItemsForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#
#         context = {
#             'form': form
#         }
#         return render(request, 'ramaelectric/test_create.html',  context)


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







