from django.db import models

class Transfer(models.Model):
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    passengers = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
