from django.db import models

# Create your models here.
class User(models.Model): # Model을 상속받는다
	name = models.CharField(max_length=20)
	description = models.TextField()
	age = models.PositiveIntegerField(null=True)
	gender = models.CharField(max_length=10)