from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .forms import ContactForm
from django.views.generic import ListView, DetailView
from products.models import Product



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
    if request.is_ajax():
        return JsonResponse({'message': 'Thank you'})
    return render(request, 'contact.html', context)
    

def homepage(request):
    return render(request, "home.html")


