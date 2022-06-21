from functools import partial
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import EmployeeSerializer

class EmployeeApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk 
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)

        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Update Completed.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    def patch(self, request, pk, format=None):
        id = pk
        emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        emp = Employee.objects.get(pk = id)
        emp.delete()
        return Response({'msg':"Data Delete Succesfully"})
