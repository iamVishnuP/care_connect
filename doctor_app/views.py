from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import authentication,permissions


from doctor_app.models import Doctor
from doctor_app.serializers import DoctorSerializer


# Create your views here.

class DoctorListCreateView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]
    def get(self,request):
        qs=Doctor.objects.all()
        serialiser_instance=DoctorSerializer(qs,many=True)
        return Response(serialiser_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=DoctorSerializer(data=form_data)
        if serializer_instance.is_valid():
            # cleaned_data= serializer_instance.validated_data
            # Doctor.objects.create(**cleaned_data)
            # response_data={"message":"created succesfully"}
            # return Response(response_data)

            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class DoctorRetreiveUpdateDeleteView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]
    def get(self,request,pk=None):
        qs=Doctor.objects.get(id=pk)
        serializer_instance= DoctorSerializer(qs)
        return Response(serializer_instance.data)

    def put(self,request,pk=None):
        form_data=request.data
        doctor_object= Doctor.objects.get(id=pk)
        serializer_instance=DoctorSerializer(data=form_data,instance=doctor_object)
        if serializer_instance.is_valid():
            # cleaned_data=serializer_instance.validated_data
            # Doctor.objects.filter(id=pk).update(**cleaned_data)
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):
        Doctor.objects.filter(id=pk).delete()
        return Response({"message":"Deleted"})