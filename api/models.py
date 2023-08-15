from django.db import models


class UserModel(models.Model):
    name = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    number = models.TextField()
    otp = models.TextField()
    time = models.DateTimeField()
    token = models.TextField()
    profile = models.ImageField()


class ImageModel(models.Model):
    image = models.ImageField()


class EstateModel(models.Model):
    location = models.TextField()
    size = models.TextField()
    price = models.TextField()
    amenities = models.TextField()
    images = models.ManyToManyField(ImageModel)
