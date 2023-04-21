from django.db import models

# Create your models here.
class Acount(models.Model):
    name=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password=models.TextField(max_length=10)

    def __str__(self):
        return self.name