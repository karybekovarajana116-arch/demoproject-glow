from django.urls import path

from .views import (
    product_list,
    product_detail,
    add_to_cart,
    search_products,
    product_create,
    product_update,
)



urlpatterns = [

    path(
        '',
        product_list,
        name='product_list'
    ),

    path(
        'product/<int:id>/',
        product_detail,
        name='product_detail'
    ),

    path(
        'add-to-cart/<int:id>/',
        add_to_cart,
        name='add_to_cart'
    ),

    path(
        'create/',
        product_create,
        name='product_create'
    ),

    path(
        'search/',
        search_products,
        name='search_products'
    ),

    path(
        'edit/<int:id>/',
        product_update,
        name='product_update'
    ),

]
