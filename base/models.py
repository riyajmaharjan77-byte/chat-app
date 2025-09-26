from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email=models.EmailField()
    password= models.CharField(max_length=100)
    username= models.CharField(max_length=100,unique=True)
    image= models.ImageField()

class friendrequest(models.Model):
    request_user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='request')
    requested_by_user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='requested_by')
    status=models.CharField(max_length=200,default='pending')

class Message(models.Model):
    receiver=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='receiver_user')
    sender=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='sender_user')
    message=models.TextField()
