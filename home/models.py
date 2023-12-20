from django.db import models

# Create your models here.
class Users(models.Model):
    email=models.EmailField(max_length=30)
    pasword=models.CharField(max_length=50)

class Person(models.Model):
    First_name=models.CharField(max_length=70)
    Last_name=models.CharField(max_length=70) 

class Groupinfo(models.Model):
    ledname=models.CharField(max_length=50,default='username',editable=False)
    ledroll=models.CharField(max_length=50,default='000000',editable=False)
    mem1=models.CharField(max_length=50,default='username',editable=False)
    mem1roll=models.CharField(max_length=50,default='000000',editable=False)
    mem2=models.CharField(max_length=50,default='username',editable=False)
    mem2roll=models.CharField(max_length=50,default='000000',editable=False)
    mem3=models.CharField(max_length=50,default='username',editable=False)
    mem3roll=models.CharField(max_length=50,default='000000',editable=False)
    

    class Meta:
        db_table="GroupInfo"

class projectinfo(models.Model):
    pname=models.CharField(max_length=50,default='username',editable=False)
    pdomain=models.TextField(default='000000',editable=False)
    pguide=models.CharField(max_length=200,default='username',editable=False)
     

    class Meta:
        db_table="projectinfo"

