from django.db import models

# Create your models here.

class ModelB(models.Model):
    A1 = models.CharField(max_length=20, null= False, blank= False)
    B1 = models.CharField(max_length=20, null= False, blank= False)
    C1 = models.CharField(max_length=20, null= False, blank= False)
    D1 = models.CharField(max_length=20, null= False, blank= False)

class ModelC(models.Model):
    A1 = models.CharField(max_length=20, null= False, blank= False)
    B1 = models.CharField(max_length=20, null= False, blank= False)
    C1 = models.CharField(max_length=20, null= False, blank= False)
    D1 = models.CharField(max_length=20, null= False, blank= False)
