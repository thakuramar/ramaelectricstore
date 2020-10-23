from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    completed = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


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

