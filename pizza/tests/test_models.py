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

        obj = PizzaMenu()

        self.order1 = Order.objects.create(
            product=obj.name("pizza1"),
            customer="user1",
            quantity=2,
            total_price=20,
            in_cart="True",
            completed="False",
        )

    def test_create_menu_product(self):
        self.assertEqual(self.pizza1.name, "pizza1")
        self.assertEqual(self.pizza1.description, "pizza1 description")
        self.assertEqual(self.pizza1.ingredients, "aaa1")
        self.assertEqual(self.pizza1.price, 10)

    def test_create_order(self):
        self.assertEqual(self.order.product, "pizza1")
