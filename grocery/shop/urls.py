from django.urls import path
from . import views

urlpatterns = [
    path("shopkeeper/", views.shopkeeper, name="shopkeeper"),
    path("customer/", views.customer, name="customer"),
]
