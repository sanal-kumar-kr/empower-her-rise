from django.db import models
from authentication.models import*
# Create your models here.
class healthcheckup(models.Model):
    userid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='osfsdiop')
    title = models.CharField(max_length=50,default='')
    description = models.TextField(default='')
    place = models.CharField(max_length=50,default='')
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

class Schemas(models.Model):
    userid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='osdfsdiop')
    title = models.CharField(max_length=50,default='')
    link = models.CharField(max_length=250,default='')

    description = models.TextField(default='')
    required = models.TextField(default='')






