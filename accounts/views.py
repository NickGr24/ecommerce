from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from .forms import LoginForm, RegisterForm
from django.utils.http import is_safe_url
from ecommerce.views import homepage

User = get_user_model()
 
def guest_register_view(request):
    template_name = 'guestform'
    form = GuestForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        return redirect(homepage)
    else:
        print('Error')            
    return redirect('/register/')

def login_page(request):
    form = LoginForm(request.POST or None)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    context = {
        "form": form,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(homepage)
            try:
                del request.session['guest_email_id']
            except:
                pass
        else:
            print('Error')            
    return render(request, "auth/login.html", context)
 
def reg_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(email=email, password=password)
    return render(request, "auth/reg.html", context)

