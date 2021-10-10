from typing import ClassVar
from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140)
    course = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']