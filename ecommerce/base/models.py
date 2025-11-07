from django.db import models

class producttype(models.Model):
    name=models.CharField(max_length=200)

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.FloatField()
    stock=models.IntegerField()
    type=models.ForeignKey(producttype,on_delete=models.SET_NULL,null=True)

class mailing(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    rating=models.IntegerField()
