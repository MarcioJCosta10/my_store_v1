from django.shortcuts import render

from .models import Cart


def cart_home(request):

    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for product in products:
      total += product.price
      print(total)
      cart_obj.total = total
      cart_obj.save()
      
    context = {
      'cart_obj': cart_obj,
      'total_cart' : cart_obj.total
               }

    return render(request, "carts/home.html", context)
