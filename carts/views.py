from django.shortcuts import render

# Create your views here.


def cart_home(request):
    print(request.session)
    print(dir(request.session))
    key = request.session.session_key
    print(key)
    request.session['card_id'] = 123
    test = request.session['user']=request.user.username
    context = {
      'teste': test
      }
    return render(request, "carts/home.html", context)
