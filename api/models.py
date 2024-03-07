from django.db import models

class Person(models.Model):
    name: str = models.CharField(max_length=100)
    age: int = models.IntegerField()
    date_of_birth: datetime.date = models.DateField()

# Create your models here.
