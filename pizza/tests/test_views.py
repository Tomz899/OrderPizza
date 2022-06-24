from django.test import TestCase


class PizzaViewsTest(TestCase):
    def test_pizza_menu_url_and_context(self):
        resp = self.client.get("http://localhost:8000/menu/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("pizza_menu" in resp.context)
