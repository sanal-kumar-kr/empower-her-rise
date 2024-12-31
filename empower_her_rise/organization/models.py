from django.db import models
from authentication.models import *
from django.utils import timezone

# Create your models here.
class courses(models.Model):
    userid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='oiopetertyer')
    courceimage=models.FileField(null=True)
    title = models.CharField(max_length=50,default='')
    description = models.TextField(default='')
    Fees = models.IntegerField(null=True)
    Duration = models.CharField(max_length=50,default='')

class Jobs(models.Model):
    userid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='oweriop')
    firmimage=models.FileField(null=True)
    firm_name = models.CharField(max_length=50,default='')
    location = models.CharField(max_length=50,default='')
    title = models.CharField(max_length=50,default='')
    description = models.TextField(default='')
    email = models.EmailField(max_length=50,default='')
    qualification = models.TextField(null=True)
    address = models.TextField(null=True)


class hostals(models.Model):
    userid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='oirewop')
    hostalimage=models.FileField(null=True)
    hostal_name = models.CharField(max_length=50,default='')
    location = models.CharField(max_length=50,default='')
    address = models.TextField(null=True)
    Rent = models.IntegerField(null=True)
    Tenant_preferred = models.TextField(null=True)
    contact = models.IntegerField(null=True)
    rule = models.TextField(null=True)
    facilities = models.TextField(null=True)


class enroll(models.Model):
    userid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='oireterwtwop')
    cource = models.ForeignKey(courses,on_delete=models.CASCADE,null=True,related_name='oirewop')
    certificate=models.FileField(null=True)
    status = models.IntegerField(null=True,default=0)

class hostalfeedback(models.Model):
    hostalid = models.ForeignKey(hostals,on_delete=models.CASCADE,null=True,related_name='oirtryguhijofrewgfrewuketerwtwop')
    userid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='oirtryguhijoketerwtwop')
    feedback = models.TextField(null=True)
    current_timestamp = timezone.now()
    ratings = models.IntegerField(null=True)


class coursevideo(models.Model):
    courseid = models.ForeignKey(courses,on_delete=models.CASCADE,null=True,related_name='fdfff')
    classvideo = models.FileField(null=True)

class courseexams(models.Model):
    current_time =models.DateTimeField(null=True)

    courseid = models.ForeignKey(courses,on_delete=models.CASCADE,null=True,related_name='yyrrr')
    link = models.CharField(max_length=250,default='')




