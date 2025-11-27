from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(null=True , blank=True)
    price = models.DecimalField(decimal_places=6 , max_digits=8)

    def __str__(self) -> str:
        return f"{self.name} - ${self.price}"





