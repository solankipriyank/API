from django.db import models

# Create your models here.
class Employee(models.Model):
	employee_name=models.CharField(max_length=100,blank=True)
	employee_department=models.PositiveIntegerField()
	salary=models.PositiveIntegerField()
	job=models.CharField(max_length=100,blank=True)

	def __str__(self):
		return self.employee_name
