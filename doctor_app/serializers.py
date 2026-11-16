from rest_framework import serializers
from doctor_app.models import Doctor

class DoctorSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    phone=serializers.CharField()
    age=serializers.CharField()
    specialization=serializers.CharField()
    consultation_fee=serializers.DecimalField(max_digits=10,decimal_places=2,default=0)
    experience=serializers.IntegerField()
    available_from=serializers.TimeField()
    available_to=serializers.TimeField()
    appointment_duration=serializers.IntegerField(default=0)

    def create(self,validated_data):
        return Doctor.objects.create(**validated_data)

    def update(self,instance,validated_data):
        for attribute,values in validated_data.items():
                setattr(instance,attribute,values)
        instance.save()
        return instance