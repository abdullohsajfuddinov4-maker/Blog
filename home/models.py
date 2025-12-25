from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project/',blank=True,null=True)
    desc = models.TextField()

