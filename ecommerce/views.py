from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from .forms import ContactForm, RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, get_user_model

def contact_page(request):
    return render(request, "contacts.html", {})

def about_page(request):
    context = {
        'title': 'About us'
    }
    return render(request, "about.html", context )

User = get_user_model()

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(form.cleaned_data)
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            return redirect("/login")
            
    return render(request, "auth/login.html", context)

 


def reg(request):
    form = RegistrationForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/reg.html", context)


def home_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "form": contact_form,
        "cleaned_email": LoginForm.clean_email,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "home_page.html", context)


