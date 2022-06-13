from django.contrib import admin

from .models import Order, PizzaMenu

admin.site.register(PizzaMenu)
admin.site.register(Order)
