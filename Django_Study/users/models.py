from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): # Model을 상속받는다
	is_business=models.BooleanField(default=False)
	grade=models.CharField(max_length=10, default='C')