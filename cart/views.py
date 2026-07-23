from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem


@login_required
def cart_view(request):
    # Фильтруем товары строго для текущего вошедшего пользователя!
    items = CartItem.objects.filter(user=request.user)

    total = sum(item.total_price() for item in items)

    context = {
        'items': items,
        'total': total,
    }
    return render(request, 'cart/cart.html', context)


@login_required
def cart_remove(request, item_id):
    # Удаляем товар только если он принадлежит текущему пользователю
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart_view')