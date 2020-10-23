from django import forms
from .models import Test, AppointmentForm, ContactPage


class TestForm(forms.ModelForm):
    class Meta:
        Model = Test
        fields = [
            'name',
            'description'
        ]


class FormAppointmentForm(forms.ModelForm):     # appointment booking form
    class Meta:
        model = AppointmentForm
        fields = '__all__'


class ContactPageForm(forms.Form):            # ContactForm for  contact page
    name = forms.CharField(max_length=25)
    phone = forms.CharField(max_length=12)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)



