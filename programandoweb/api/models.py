from csv import unregister_dialect
from django.db import models
from django.forms import PasswordInput
class Pgrw_User(models.Model):
    names       =   models.CharField(max_length=30)
    lastnames   =   models.CharField(max_length=30)
    email       =   models.CharField(max_length=150)
    password    =   models.CharField(max_length=250)  

