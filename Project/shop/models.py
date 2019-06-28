from django.db import models
from django.conf import settings


class Users(models.Model):
	username=models.CharField(max_length=30)
	email=models.CharField(max_length=50)
	password=models.CharField(max_length=20)

class Login(models.Model):
	username=models.CharField(max_length=30)
	password=models.CharField(max_length=20)

class Products(models.Model):
	product_name=models.CharField(max_length=100)
	product_description=models.TextField()
	photo=models.ImageField(upload_to='product_image')


