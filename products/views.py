from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ProductForm
from .models import Product, Category
from cart.models import CartItem


def product_list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})


@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    # Ищем или создаем товар ИМЕННО для текущего залогиненного пользователя
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    # Если такой товар уже был в корзине этого пользователя — просто увеличиваем количество
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')


def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.none()

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query) |
            Q(description__icontains=query)
        )

    context = {
        'query': query,
        'products': products,
    }
    return render(request, 'products/search_results.html', context)


@login_required
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'products/product_create.html', {'form': form})


@login_required
def product_update(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', id=product.id)
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        'products/product_update.html',
        {
            'form': form,
            'product': product
        }
    )