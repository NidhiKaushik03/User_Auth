
from django.db import models

# Create your models here.

class Emp_Info(models.Model):
    Fullname = models.CharField(max_length=100)
    Salary = models.IntegerField()
    Address= models.CharField(max_length=100)
    Status= models.BooleanField()



    # def __str__(self):
    #     return(self.Fullname)


    # class Meta:
    #     verbose_name = "Banglore"

        
    