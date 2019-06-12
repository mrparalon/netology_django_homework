from django.db import models


class Car(models.Model):
    brand = models.TextField()
    name = models.TextField()
    color = models.TextField()

class Person(models.Model):
    name = models.CharField(max_length=128)
    gender = models.CharField(max_length=16)
    birthday = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
