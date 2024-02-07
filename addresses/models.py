from django.db import models

from billing.models import BillingProfile


ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shupping', 'Shipping'),
)


class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=150, choices=ADDRESS_TYPES)
    address = models.CharField(max_length=150, verbose_name='Adresa')
    city = models.CharField(max_length=150, verbose_name='Oraș')
    state = models.CharField(max_length=100, verbose_name='Țară', default='Moldova')
    postal_code = models.CharField(max_length=150, verbose_name='Cod poștal')
    
    def __str__(self):
        return str(self.billing_profile)


