from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=3, default=39.9)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True, db_index=True, verbose_name="URL")
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', args=[self.slug])
        
class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None