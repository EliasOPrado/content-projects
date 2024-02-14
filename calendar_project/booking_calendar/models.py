from django.db import models

class Availability(models.Model):
    availability_date = models.DateField()

class AvailableDay(models.Model):
    day = models.DateField(unique=True)
    is_available = models.BooleanField(default=True)

class Booking(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Availability(models.Model):
    availability_date = models.DateField()