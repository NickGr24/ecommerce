from django.db import models

from cart.models import Cart


STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('annulated', 'Annulated')
)

class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    status = models.CharField(max_length=50, default='created', choices=STATUS_CHOICES)
    shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
   
    def __str__(self):
        return self.order_id