from django.db import models

from billing.models import BillingProfile


ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shupping', 'Shipping'),
)


class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=150, choices=ADDRESS_TYPES)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=100, default='Moldova')
    postal_code = models.CharField(max_length=150)
    
    def __str__(self):
        return str(self.billing_profile)


