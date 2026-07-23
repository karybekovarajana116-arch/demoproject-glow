from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def checkout(request):
    if request.method == "POST":
        Order.objects.create(
            user=request.user,
            name=request.POST['name'],
            email=request.POST['email'],
            address=request.POST['address']
        )

        return render(request, 'orders/success.html')

    return render(request, 'orders/checkout.html')