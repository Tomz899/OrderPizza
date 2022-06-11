from django.urls import path

from pizza.views import (
    IndexView,
    PizzaMenuListView,
    About,
    PizzaDetailView,
    LoginView,
    LogoutView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("menu/", PizzaMenuListView.as_view(), name="menu"),
    path("about/", About.as_view(), name="about"),
    path("pizza/<int:pk>/", PizzaDetailView.as_view(), name="pizza_detail"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]