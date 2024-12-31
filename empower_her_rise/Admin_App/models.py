from django.db import models
from authentication.models import *
from django.utils import timezone
from authentication.models import *
from .models import *

classt=[
    ('','Select'),
    ('online','online'),
    ('offline','offline')
]

# Create your models here.
class Talentgroup(models.Model):
    title = models.CharField(max_length=50,default='')
    description = models.TextField(default='')


class classes(models.Model):
    userid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='gftftyfftyfuoiop')
    title = models.CharField(max_length=50,default='')
    description = models.TextField(max_length=50,default='')
    start_time=models.TimeField(null=True)
    end_time=models.TimeField(null=True)
    date=models.DateField(null=True)
    amount=models.IntegerField(null=True)
    place = models.CharField(max_length=50,default='')
    class_type= models.CharField(max_length=50,default='',choices=classt)


class inbox(models.Model):
    sender = models.ForeignKey(Register, related_name='service_person', on_delete=models.CASCADE, null=True)
    reciever = models.ForeignKey(Register, related_name='org_id', on_delete=models.CASCADE, null=True)
    message = models.TextField(null=True)
    datetime=models.DateTimeField(null=True)
    status = models.IntegerField(null=True, default=0)


class members(models.Model):
    userid = models.ForeignKey(Register, related_name='service_WDEWQperson', on_delete=models.CASCADE, null=True)
    gpid = models.ForeignKey(Talentgroup, related_name='orgWEWRE_id', on_delete=models.CASCADE, null=True)
    status = models.IntegerField(null=True, default=0)

       
class classvideo(models.Model):
    classid = models.ForeignKey(classes, related_name='ertewrtwert', on_delete=models.CASCADE, null=True)
    video = models.FileField(null=True)


class booking(models.Model):
    user = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='sdassigfhjkadgtsdgghjd')
    classid = models.ForeignKey(classes,on_delete=models.CASCADE,null=True,related_name='adssigfetwrtewrthjkghjd')
    status=models.IntegerField(null=True,default=0)

class feedback(models.Model):
    userid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='sdassigfhdfhydfhetjkadgtsdgghjd')
    classid = models.ForeignKey(classes,on_delete=models.CASCADE,null=True,related_name='adssigfetwtetrterrtewrthjkghjd')
    feedback =models.TextField(null=True)
    reply=models.TextField(null=True)
    status=models.IntegerField(null=True,default=0)


class groupinbox(models.Model):
    sender = models.ForeignKey(Register, related_name='sdr', on_delete=models.CASCADE, null=True)
    groupid = models.ForeignKey(Talentgroup, related_name='sdererr', on_delete=models.CASCADE, null=True)

    message = models.TextField(null=True)
    datetime=models.DateTimeField(null=True)





