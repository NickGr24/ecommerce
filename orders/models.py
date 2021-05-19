from django.db import models

from django.db.models.signals import pre_save, post_save

from cart.models import Cart

from addresses.models import Address

from billing.models import BillingProfile

import math

from ecommerce.utils import unique_slug_generator

STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('annulated', 'Annulated')
)


class OrderManager(models.Manager):
    
    def new_or_get(self, billing_profile, cart_obj):
        qs = self.get_queryset().filter(cart=cart_obj, active=True)
        if qs.count() == 1:
            created = False
            obj = qs.first()

        else:
            obj = Order.objects.create(cart=cart_obj, billing_profile=billing_profile)
            created = True
        return obj, created



class Order(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE, blank=True, null=True)
    order_id = models.CharField(max_length=120, blank=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=50, default='created', choices=STATUS_CHOICES)
    shipping_total = models.DecimalField(default=5.9, max_digits=10, decimal_places=1)
    total = models.DecimalField(default=5.9, max_digits=10, decimal_places=1)
    active = models.BooleanField(default=True)
    
    objects = OrderManager()

    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total = self.cart.total
        shipping_total = self.shipping_total
        new_total = math.fsum([cart_total,  shipping_total])
        self.total = new_total
        self.save()
        return new_total

def pre_save_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_slug_generator(instance)
    qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        qs.update(active=False)

pre_save.connect(pre_save_order_id, sender=Order)

def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1 :
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total, sender=Cart)

def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()

post_save.connect(post_save_order, sender=Order)