from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    age=models.CharField(max_length=2)
    specialization=models.CharField(max_length=200)
    consultation_fee=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    experience=models.PositiveIntegerField()
    available_from=models.TimeField(default="09:00:00")
    available_to=models.TimeField(default="17:00:00")
    appointment_duration=models.PositiveIntegerField(default=0)