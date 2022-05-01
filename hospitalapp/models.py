
from django.db import models

# Create your models here.
class patient(models.Model):
    name=models.CharField(max_length=90)
    phno=models.CharField(max_length=80)
    email=models.EmailField(max_length=80,default=None)
    Disease=models.CharField(max_length=70)
    Description=models.TextField(max_length=900)
    password=models.CharField(max_length=50,default=None,blank=True,null=True)
    
     
   
class doctor(models.Model):
    name=models.CharField(max_length=30)
    id_no=models.PositiveIntegerField()
    email=models.EmailField(max_length=70,default=None)
    password=models.CharField(max_length=10)
 

