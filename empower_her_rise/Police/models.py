from django.db import models

# Create your models here.
class selfdefenceclasses(models.Model):
    title = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=50,default='')
    place = models.CharField(max_length=50,default='')
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    class_type=models.CharField(max_length=50,default='')