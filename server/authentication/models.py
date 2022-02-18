from django.db import models

# Create your models here.

class register(models.Model):
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 30)
    email = models.EmailField()
    password = models.CharField(max_length = 20)
    cpassword = models.CharField(max_length = 20)
    pnum = models.IntegerField()
    
