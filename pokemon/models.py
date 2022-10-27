from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Pokemon(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    base_experience = models.FloatField()

    def __str__(self):
        return f"{self.name}"
