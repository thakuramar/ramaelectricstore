from django.db import models

# Items model for importing excel or csv file directly through admin panel & convert into model data and same data shows into service page. 


class Items(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    model_type = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    arrival_date = models.CharField(max_length=10 , blank=True, null=True)
    img = models.ImageField(upload_to='images', blank=True, null=True)

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

