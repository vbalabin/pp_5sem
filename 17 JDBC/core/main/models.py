from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.TextField(max_length=64)
    position = models.TextField(max_length=64)
    enlisted = models.DateField()
    department = models.TextField(max_length=64)
    is_active = models.BooleanField(default=True)
