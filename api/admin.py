from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','emp_name', 'emp_id', 'emp_age', 'emp_add']
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']