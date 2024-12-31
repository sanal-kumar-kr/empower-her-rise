from django.db import models
from django.contrib.auth.models import AbstractUser
state=[
    ('','Select'),
    ('Kerala','Kerala')
]


district=[
    ('','Select'),
    ('Thrissur','Thrissur')
]


gender=[
    ('','Select'),
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),

]


class Register(AbstractUser):
    name = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50,default='')
    contact = models.IntegerField(null=True)
    houseno = models.CharField(max_length=50,default='')
    street = models.CharField(max_length=50,default='')
    description = models.TextField(default='')
    id_proof = models.FileField(null=True, upload_to='id_proof/')
    gender = models.CharField(max_length=50,default='',choices=gender)
    qualification = models.CharField(max_length=50,default='')
    yearofexperience = models.CharField(max_length=50,default='')
    district = models.CharField(max_length=50,default='',choices=district)
    state = models.CharField(max_length=50,default='',choices=state)
    rank = models.CharField(max_length=50,default='')
    usertype=models.IntegerField(null=True,default=1)
    pin=models.IntegerField(null=True)

    status=models.IntegerField(null=True,default=1)

    
    
class chat(models.Model):
    senderid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='sid')
    recieverid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='rid')
    messsage = models.FileField(max_length=50,default='')
    
# class DHORegister(models.Model):
#     DHOname = models.CharField(max_length=50,default='')
#     email = models.CharField(max_length=50,default='')
#     gender = models.CharField(max_length=50,default='')
#     qualification = models.CharField(max_length=50,default='')
#     yearofexperience = models.CharField(max_length=50,default='')
#     contact = models.IntegerField(null=True)
#     district = models.CharField(max_length=50,default='')
#     state = models.CharField(max_length=50,default='')
#     id_proof = models.FileField(null=True, upload_to='id_proof/')
    



   
   