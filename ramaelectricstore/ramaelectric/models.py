from django.db import models
from django.urls import reverse

# testing model for importing excel or csv file directly through admin panel & convert into model data


class Items(models.Model):
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20, blank=True, null=True)
    item = models.CharField(max_length=20, blank=True, null=True)
    delivery = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    model_type = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    arrival_date = models.CharField( max_length=20, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True, editable=False)
    img = models.ImageField(upload_to='images/', blank=True, null=True, default='/images/logo.jpg')

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    # @property
    # def image_url(self):
    #     if self.img:
    #         return self.img.url
    #     return '#'


class AppointmentForm(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    message = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    schedule = models.CharField(max_length=50)
    day = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class ContactPage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

