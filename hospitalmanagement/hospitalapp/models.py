from django.db import models
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    did=models.CharField(max_length=20)
    department=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    dphno=models.IntegerField(max_length=20)
    password=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    address=models.CharField(max_length=20)

class Patient(models.Model):
    name=models.CharField(max_length=50)
    pid=models.CharField(max_length=20)
    cause=models.CharField(max_length=50)
    pphno=models.BigIntegerField(max_length=20)
    address=models.CharField(max_length=20)
    feedback=models.CharField(max_length=50)
