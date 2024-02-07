from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django import forms
from .forms import ContactForm
from products.models import Product
from ipware import get_client_ip
from accounts.models import UserIPAddress

def about_page(request):
    context = {
        'title': 'About us'
    }
    return render(request, "about.html", context)


def contact_page(request):
    form = ContactForm
    context = {
        'form': ContactForm
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'message': 'Vă mulțumim!'})
    return render(request, 'contact.html', context) 
    
def homepage(request):
    client_ip = get_client_ip(request)
    client_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
    accept_language = request.META.get('ACCEPT_LANGUAGE', 'Unknown')
    UserIPAddress.objects.create(ip_address=client_ip, user_agent=client_agent, user_language=accept_language)
    return render(request, 'home.html')


