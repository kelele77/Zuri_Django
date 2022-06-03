from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=23)
    adress = models.CharField(max_length=23)

    def __str__(self) -> str:
        return self.name

class Church(models.Model):
    name = models.CharField(max_length=23)

    def __str__(self) -> str:
        return self.name
