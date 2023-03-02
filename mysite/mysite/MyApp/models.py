from django.db import models
GENDER_CHOICES=(
    ( "0","Male"),
    ("1","Female"))
class Intern(models.Model):
    First_name = models.CharField(max_length=15)
    Last_name = models.CharField(max_length=15)
    email =models.EmailField(max_length=20)
    gender=models.IntegerField(choices=GENDER_CHOICES, default='1')
    dateofbirth =models.DateField()

        

