from django.db import models


# Create your models here.
class Details(models.Model):
    place_name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()

    def __str__(self):
        return self.place_name


class Reviews(models.Model):
    client_name = models.CharField(max_length=250)
    client_photo = models.ImageField(upload_to='picture')
    client_location = models.CharField(max_length=100)
    reviews = models.TextField()

    def __str__(self):
        return self.client_name
