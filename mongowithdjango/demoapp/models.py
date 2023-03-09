from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=50)
    description = models.CharField(max_length=500)


    def __str__(self):
        return self.task

class MoneyExpence(models.Model):
    reason = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date = models.DateField(max_length=10)
    prise = models.IntegerField(max_length=20)


    def __str__(self):
        return self.reason
        
