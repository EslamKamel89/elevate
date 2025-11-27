from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(null=True , blank=True)
    price = models.DecimalField()

    def __str__(self) -> str:
        return f"{self.name} - ${self.price}"





