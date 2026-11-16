from reservation.models import Appointment
from rest_framework import serializers
from datetime import datetime

from doctor_app.models import Doctor

class AppointmentSerializer(serializers.Serializer):

        id=serializers.IntegerField(read_only=True)

        name = serializers.CharField(max_length=150)
    
        phone = serializers.CharField(max_length=10)
    
        email=serializers.EmailField()
    
        doctor=serializers.IntegerField()
    
        token=serializers.IntegerField(read_only=True)
    
        appointment_date=serializers.DateField()
    
        appointment_time=serializers.TimeField(read_only=True)

        fee=serializers.DecimalField(max_digits=10,decimal_places=2,read_only=True)

        def create(self, validated_data):
                return Appointment.objects.create(**validated_data)

        def update(self, instance, validated_data):
                for attribute,values in validated_data.items():
                        setattr(instance,attribute,values)
                instance.save()
                return instance

        def validate(self, validated_data):
                doctor_id= validated_data.get("doctor")
                if not Doctor.objects.filter(id=doctor_id).exists():
                        raise serializers.ValidationError("Doctor Not Exists...")

                appointment_date=validated_data.get("appointment_date")
                if appointment_date < datetime.today().date():
                        raise serializers.ValidationError("Invalid appointment date...")
                return validated_data