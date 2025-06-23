from django.db import models

# Create your models here.
class Board(models.Model):  # 단수표현!
    title = models.CharField(max_length=30)
    content = models.TextField()