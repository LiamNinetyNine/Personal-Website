# Create your models here.
from django.db import models


class Project(models.Model): #the self of this class is the models.Model
    project_name = models.CharField(max_length=200)
    project_url = models.CharField(max_length=200)