from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from reservation.serializers import AppointmentSerializer

from doctor_app.models import Doctor

from reservation.models import Appointment

from datetime import datetime,time,timedelta


# Create your views here.
class AppointmentView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request):
        form_data=request.data
        serializer_instance= AppointmentSerializer(data=form_data)
        if  serializer_instance.is_valid():
            cleaned_data= serializer_instance.validated_data
            doctor_id= cleaned_data.get("doctor")
            form_object= Doctor.objects.get(id=doctor_id)
            appointment_date = cleaned_data.get("appointment_date")
            appointment_duration=cleaned_data.get("appointment_duration")

            # Token generation
            last_appointment = Appointment.objects.filter(
                doctor=doctor_id,
                appointment_date=appointment_date
            ).order_by("-token").first()

            if last_appointment:
                token = last_appointment.token + 1
            else:
                token = 1

            # Appointment time calculation
            if last_appointment:
                appointment_time = last_appointment.appointment_time

                appointment_date_time = (
                    datetime.combine(appointment_date, appointment_time)
                    + timedelta(minutes=appointment_duration)
                )

                appointment_time = appointment_date_time.time()

            else:
                appointment_time = form_object.available_from

            fee= form_object.consultation_fee


            # appointment_object=Appointment.objects.filter(
            #     doctor=cleaned_data.get("doctor"),
            #     appointment_date=cleaned_data.get("appointment_date"),
            #     appointment_time__gt=appointment_time
            #       )
            # if appointment_object.exists():
            #     return Response({"message":"slot not available..."})

            # last_appointment= Appointment.objects.filter(
            #     doctor=doctor_id,
            #     appointment_date=appointment_date
            # ).order_by().first()

            # if last_appointment:
            #     appointment_time=last_appointment.appointment_time
            # else:
            #     appointment_time=form_object.available_from

            serializer_instance.save(token=token, appointment_time=appointment_time, fee=fee)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


class AppointmentRetrieveUpdateDeleteView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk=None):
        qs= Appointment.objects.get(id=pk)
        serializer_instance=AppointmentSerializer(qs)
        return Response(serializer_instance.data)

    def put(self,request,pk=None):
        form_data=request.data
        form_object=Appointment.objects.get(id=pk)
        serializer_instance=AppointmentSerializer(data=form_data,instance=form_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):
        Appointment.objects.filter(id=pk).delete()
        return Response({"message":"deleted"})


class AppointmentSummaryView(APIView):

    def post(self,request):

        form_data=request.data
        doctor=form_data.get("doctor")
        appointment_date=datetime.strptime(form_data.get("appointment_time"),"%Y-%m-%d")
        
        #appointment_date=form_data.get("appointment_time")
        appointments= Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date)
        serializer_instance=AppointmentSerializer(appointments,many=True)
        return Response(serializer_instance.data)

    
