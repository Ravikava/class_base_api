from dataclasses import fields
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','emp_name','emp_id', 'emp_age', 'emp_add']