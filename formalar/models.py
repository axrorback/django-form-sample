from django.db import models

# Create your models here.


class Savollar(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name