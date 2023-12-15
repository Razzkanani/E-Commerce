from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=20, unique=True)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return self.name