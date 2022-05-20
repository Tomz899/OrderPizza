from django.db import models


class PizzaMenu(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    ingredients = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["price"]
