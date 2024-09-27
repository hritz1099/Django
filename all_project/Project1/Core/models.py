from django.db import models
from Core.models import *
# from .forms import *
from django.shortcuts import render

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    age=models.IntegerField()
    mobileNo=models.IntegerField()
    dob=models.DateField(null=True,blank=True)
    pic=models.ImageField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    last_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Course(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    student=models.ManyToManyField(Student,null=True,blank=True)
    def __str__(self):
        return self.name
    
class PaymentDetails(models.Model):
    amount=models.IntegerField()
    payment_mode=models.CharField(max_length=100,choices=[('Cash','Cash'),('Debit Card','Debit Card'),('Credit Card','Credit Card'),('UPI','Pay UPI')])#pending
    payment_date=models.DateTimeField(auto_now=True)
    # {s should be small }student=models.ForeignKey(Student,null=False,blank=False)
    student=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE,default=1)



