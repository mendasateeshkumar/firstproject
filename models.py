from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=35)
    emp_phno=models.BigIntegerField()
    emp_mailid=models.CharField(primary_key=True, max_length=40)
    emp_password=models.CharField(max_length=35)


class Books(models.Model):
    Book_name=models.CharField(max_length= 100)