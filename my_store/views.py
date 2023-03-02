from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import date



from .forms import ContactForm

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
  
def home_page(request):
    context = {
                    "title": "SheBanG #️⃣❗️",
                    "content": "welcome!",
              }
    if request.user.is_authenticated:
        data_atual = date.today()
        print(data_atual)
        context["premium_content"] = data_atual
        context["emojiStar"] = "✨"
    return render(request, "home_page.html", context)
    
def about_page(request):
    context = {
                    "title": "Página Sobre",
                    "content": "Bem vindo a página sobre"
              }
    return render(request, "about/view.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
                    "title": "Página de Contato 📬",
                    "content": "Preencha os campos abaixo e envie sua mensagem, responderemos o quanto antes. 🧑‍💻",
                    "form": contact_form	
              }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if is_ajax(request):
            return JsonResponse({"message": "Obrigado!"})
    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if is_ajax(request):
            return HttpResponse(errors, status=400, content_type='application/json')

    return render(request, "contact/view.html", context)