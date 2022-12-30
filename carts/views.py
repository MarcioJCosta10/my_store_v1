from django.shortcuts import render
from .models import Cart

# Create your views here.


def cart_home(request):
    cart_obj = Cart.object.new_or_get(request)
    context = {'cart_obj': cart_obj}
    return render(request, "carts/home.html", context)
