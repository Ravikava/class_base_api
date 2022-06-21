from django.db import models

# creating a datatable of employee

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_id = models.IntegerField()
    emp_age = models.IntegerField()
    emp_add = models.CharField(max_length=100)