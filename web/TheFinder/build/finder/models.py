from django.db import models
from django.contrib.auth.models import User

class AcademicDivision(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    course = models.ManyToManyField('Course', related_name="academic_divisions")

    def __str__(self):
        return self.name
    
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    employee = models.ManyToManyField('Employee', related_name="departments")

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ManyToManyField('Department', related_name="employees")
    is_admin = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,  null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ManyToManyField('Employee', related_name="courses")
    
    def __str__(self):
        return self.name
    
