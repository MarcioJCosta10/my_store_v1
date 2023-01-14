
from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.views import login_page, logout_page

from .forms import ContactForm
from accounts.forms import RegisterForm


def home_page(request):
    print(request.session.get('first_name', 'Unknow'))

    context = {
        "title": "Home Page",
        "content": "Bem vindo a Home Page",
    }
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "Página sobre",
        "content": "Bem vindo a página sobre",
    }
    return render(request, "about/view.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Pagina de contato",
        "content": "Bem vindo a pagina de contato",
        "form": contact_form,

    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)


