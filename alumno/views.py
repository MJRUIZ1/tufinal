from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from alumno.models import Alumno
from alumno.models import Carrera

from alumno.serializer import AlumnoSerializers
from alumno.serializer import CarreraSerializer

class AlumnoList(APIView):
    
    def get(self, request, format=None):
        queryset = Alumno.objects.all()
        serializer = AlumnoSerializers(queryset, many=True)
        return Response(serializer.data)

    def get_object(self, id):
        try:
            return Alumno.objects.get(pk=id)
        except Alumno.DoesNotExist:
            return 404
            
    def post(self, request, format=None):
        serializer = AlumnoSerializers(data = request.data)
        if serializer.is_valid():
            alumno = serializer.save()
            datas = serializer.data
            id_alumno = alumno.id            
            
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AlumnoDetail(APIView):
    def get_object(self, id):
        try:
            return Alumno.objects.get(id=id)
        except Alumno.DoesNotExist:
            return 404

    def get(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != 404:
            #many = True No aplica si retorno un solo objeto
            serializer = AlumnoSerializers(alumno)
            alum = serializer.data   
          
            return Response(alum)
        else:
            return Response(alumno, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != 404:
            serializer = AlumnoSerializers(alumno, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else: 
            return Response(alumno, status = status.HTTP_404_BAD_REQUEST)

    def delete(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != 404:
            alumno.delete()
            return Response(1)
        return Response(404)

class Asignatura(APIView):
    def get(self, request, format=None):
        queryset = Carrera.objects.all()
        serializer = CarreraSerializer(queryset, many=True)
        return Response(serializer.data)



# Create your views here.
