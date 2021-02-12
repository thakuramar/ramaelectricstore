from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator, validate_email,validate_slug

# Items model for importing excel or csv file directly through admin panel & convert into model data and same data shows into service page. 


class Items(models.Model):
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20, blank=True, null=True)
    item = models.CharField(max_length=20, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
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

    def __str__(self):
        return str(self.item) + ": Rs. " + str(self.price)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class ItemsImage(models.Model):  # for uploding multiple image
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/', blank=True, null=True, default='/images/logo.jpg')

    def __str__(self):
        return self.items.name

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
    updated_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.name


class ContactPage(models.Model):
    name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?0?\d{9,13}$',
                                 message="Phone number must be in the format: '+999999999'")
    phone = models.CharField(validators=[phone_regex], max_length=13)
    email = models.EmailField(null=True, blank=True)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

