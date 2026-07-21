from django.shortcuts import render
from .models import CartItem


def cart_view(request):

    items = CartItem.objects.all()

    total = sum(
        item.total_price()
        for item in items
    )

    context = {
        'items': items,
        'total': total,
    }

    return render(
        request,
        'cart/cart.html',
        context
    )
