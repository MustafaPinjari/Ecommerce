# cart/views.py
from django.shortcuts import render
from .models import CartItem

def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart/cart.html', {'cart_items': cart_items})
