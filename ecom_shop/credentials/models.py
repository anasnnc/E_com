from django.db import models

# Create your models here.
class login(models.Model):
    username=models.EmailField()
    password=models.IntegerField()
    