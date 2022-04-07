from django.db import models


class position(models.Model):
    title  = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    emp_code = models.CharField(max_length=4)
    mobile = models.CharField(max_length=30)
    position = models.ForeignKey(position, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname



