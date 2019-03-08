from django.db import models
from 

# Create your models here

class Shop(models.Model):
    name = models.CharField(max_length=50)
    profile = models.ManyToManyField(Profile)
    url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
