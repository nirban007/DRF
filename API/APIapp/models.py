from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name