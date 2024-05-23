from django.contrib import admin
from django.urls import path
from myapp.views import EmployeeList,EmployeeDetail

urlpatterns=[

path('api/employees',EmployeeList.as_view()),
path('api/employees/<int:pk>',EmployeeDetail.as_view()),
path('admin/',admin.site.urls),
]