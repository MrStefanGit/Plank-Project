from django.db import models
from django.contrib.auth.models import AbstractUser

class Departments(models.Model):
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.department

class CustomUser(AbstractUser):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
