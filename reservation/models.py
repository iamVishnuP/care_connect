from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=150)

    phone = models.CharField(max_length=10)

    email=models.EmailField()

    doctor=models.PositiveIntegerField()

    token=models.PositiveIntegerField(null=True)

    appointment_date=models.DateField()

    appointment_time=models.TimeField(null=True)

    fee=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    
