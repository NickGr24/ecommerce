from django.db import models
from django.urls import reverse
import datetime

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=3, default=39.9)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True, db_index=True, verbose_name="URL")
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=datetime.datetime.today())

    def get_absolute_url(self):
        return reverse("products", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title

class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None