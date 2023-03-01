from django.db import models

class Intern(models.Model):
    First_name = models.CharField(max_length=15)
    Last_name = models.CharField(max_length=15)
    email =models.EmailField(max_length=20)
    dateofbirth =models.DateField()

        

