from django.contrib.auth.models import User
from django.test import TestCase
from pizza.models import Order, PizzaMenu


class PizzaMenuModelTest(TestCase):
    def setUp(self):
        self.pizza1 = PizzaMenu.objects.create(
            name="pizza1",
            description="pizza1 description",
            ingredients="aaa1",
            price=10,
        )

    def test_create_menu_product(self):
        self.assertEqual(self.pizza1.name, "pizza1")
        self.assertEqual(self.pizza1.description, "pizza1 description")
        self.assertEqual(self.pizza1.ingredients, "aaa1")
        self.assertEqual(self.pizza1.price, 10)


class OrderModelTest(TestCase):
    def setUp(self):
        # Creating pizza product
        self.pizza1 = PizzaMenu.objects.create(
            name="pizza1",
            description="pizza1 description",
            ingredients="aaa1",
            price=10,
        )

        # Creating customer
        self.user1 = User.objects.create_user("test1", "test1@testcompany.com", "pass1")

        # Instances of PizzaMenu and User test objects
        obj = self.pizza1
        test_user = self.user1

        # Creating order
        self.order1 = Order.objects.create(
            product=obj,
            customer=test_user,
            quantity=2,
            total_price=20,
            in_cart="True",
            completed="False",
        )

    def test_create_order(self):
        self.assertEqual(self.order1.product.name, "pizza1")

    def test_get_item_cost(self):
        total_cost = self.order1.quantity * self.order1.product.price
        self.assertEqual(total_cost, 20)
