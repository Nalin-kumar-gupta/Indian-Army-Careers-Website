from django.db import models

class EmployeeModel(models.Model):
    gender = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    task_force = models.CharField(max_length=100)
