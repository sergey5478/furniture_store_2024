from django.urls import path

from carts import views

app_name = "carts"

urlpatterns = [
    path("cart_add/<product_id>/", views.cart_add, name="cart_add"),
    path("cart_change/<product_id>/", views.cart_change, name="cart_change"),
    path("cart_remove/<product_id>/", views.cart_remove, name="cart_remove"),
]