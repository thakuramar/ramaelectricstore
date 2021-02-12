from django import forms
from .models import Items, AppointmentForm, ContactPage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class ItemsForm(forms.ModelForm):  # Items Form
    class Meta:
        Model = Items
        fields = '__all__'


class FormAppointmentForm(forms.ModelForm):     # appointment booking form
    class Meta:
        model = AppointmentForm
        fields = '__all__'


class ContactPageForm(forms.Form):            # ContactForm for  contact page
    name = forms.CharField(max_length=25)
    phone = forms.CharField(max_length=12)
    email = forms.EmailField(validators=[validate_email])
    message = forms.CharField(widget=forms.Textarea)







    # def clean_email(self):                                      # fields level validation
    #     email_passed = self.cleaned_data.get("email")
          #email2_passed = self.cleaned_data.get("email2")
    #       required_email = "domain.com"                      if passed email is not a domain email den also show error
    #       if not required_email in email_passed:
    #           raise forms.ValidationError("Note the valid email")
    #         if email2_passed != email_passed:                    #  if we use re-enter email
    #             raise forms.ValidationError("email not match")
    #
    #     return email_passed

    # def clean(self):                                                #  Forms level validation -- non- field -- errors
    #     cleaned_data = super(ContactPageForm,self).clean()
    #     email_passed = self.cleaned_data.get("email")
    #     required_email = "domain.com"
    #     if not required_email in email_passed:
    #         raise forms.ValidationError("Note the valid email")




