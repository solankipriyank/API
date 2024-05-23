from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Employee
		fields=('id','employee_name','employee_department','salary','job')
