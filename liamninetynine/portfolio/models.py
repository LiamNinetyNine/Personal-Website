# Create your models here.
from django.db import models
from datetime import date


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    def __str__(self):
        return self.name

class Project(models.Model):
    project = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=255)
    project_description = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    def __str__(self):
        return self.project_title