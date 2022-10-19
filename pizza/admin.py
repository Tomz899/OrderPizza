from django.contrib import admin

from .models import Order, PizzaMenu, User

admin.site.register(User)
admin.site.register(PizzaMenu)
admin.site.register(Order)
