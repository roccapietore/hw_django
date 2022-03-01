from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    is_published = models.CharField(max_length=10)


class Category(models.Model):
    name = models.CharField(max_length=25)
