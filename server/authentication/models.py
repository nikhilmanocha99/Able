from django.db import models

# Create your models here.
def register(models.Model):
    fname = models.Charfield(max_length = 30)
    lname = models.Charfield(max_length = 30)
    email = models.Emailfield()
    password = models.Passwordfield()
    cpassword = models.Passwordfield()
    pnum = models.IntegerField()