from django.shortcuts import render

# Create your views here.


def cart_home(request):
    print('Request', request)
    print('request.session', request.session)
    print('dir(request.session)', dir(request.session))
    key = request.session.session_key
    print('key', key)
    request.session['card_id'] = 123
    test = request.session['user'] = request.user.username

    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        print('Create new cart')
        request.session['cart_id'] = 12
    else:
        print('Cart_id exist')
        
    context = {
            'teste': test,
            'cart_id': cart_id
        }
    return render(request, "carts/home.html", {})
