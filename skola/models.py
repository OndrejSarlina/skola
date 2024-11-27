from django.db import models

# Create your models here.

class Student(models.Model):
    meno = models.CharField(max_length=20) # textove pole
    priezvisko = models.CharField(max_length=20)
    trieda = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.trieda}"