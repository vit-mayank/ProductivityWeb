from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length = 50)
class Students(models.Model):
    name = models.CharField(max_length = 100)
    course = models.ForeignKey(Courses, on_delete = models.CASCADE)
    