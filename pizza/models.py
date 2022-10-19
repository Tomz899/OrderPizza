from decimal import Decimal

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from pizza.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class PizzaMenu(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    ingredients = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["price"]
        verbose_name_plural = "Pizza Menu"


class Order(models.Model):
    product = models.ForeignKey(PizzaMenu, null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    order_date = models.DateTimeField(auto_now_add=True)
    in_cart = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"

    class Meta:
        ordering = ["-order_date"]

    # @property
    def get_item_cost(self):
        total_cost = self.quantity * self.product.price
        return Decimal(total_cost)
