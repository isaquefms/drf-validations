from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    phone = models.CharField(max_length=14)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.cpf}'
