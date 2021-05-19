from django.shortcuts import render
from django.shortcuts import redirect
from .forms import AddressForm
from billing.models import BillingProfile
from .models import Address
from ecommerce.views import homepage

def checkout_address_create_view(request):
    form = AddressForm(request.POST or None)
    context = {
        "form": form,
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    if form.is_valid():
        instance = form.save(commit=False)
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if billing_profile is not None:
            address_type = request.POST.get('address_type', 'shipping')
            instance.billing_profile = billing_profile
            instance.address_type = request.POST.get('address_type', 'Shipping')
            instance.save()
            return redirect(homepage)
        else:
            print('Error')
    return instance
    
