from django.urls import path

from . import views

urlpatterns = [
    path("buy/<int:pk>", views.create_item_checkout_session,
         name="item"),
    path("item/<int:pk>", views.payment_item_page),
    path("order-buy/<int:pk>", views.create_order_checkout_session,
         name="order"),
    path("order/<int:pk>", views.payment_order_page),
]
