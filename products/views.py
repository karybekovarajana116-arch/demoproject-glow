from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from cart.models import CartItem



def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'products/product_list.html', context)


from django.shortcuts import get_object_or_404


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )
def add_to_cart(request, id):

    product = get_object_or_404(Product, id=id)

    CartItem.objects.create(
        product=product
    )

    return redirect('cart')

def add_to_cart(request, id):

    product = get_object_or_404(Product, id=id)

    CartItem.objects.create(
        product=product
    )

    return redirect('cart')
