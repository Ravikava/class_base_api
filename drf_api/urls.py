from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empapi/',EmployeeApi.as_view()),
    path('empapi/<int:pk>/',EmployeeApi.as_view()),
    path('stuapi/',StudentList.as_view()),
    path('stuapi/<int:pk>/',StudentListUpdate.as_view()),
    
]
