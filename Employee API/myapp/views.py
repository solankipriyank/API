from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.

class EmployeeList(generics.ListCreateAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Employee
	serializer_class=EmployeeSerializer

# Create your views here.
