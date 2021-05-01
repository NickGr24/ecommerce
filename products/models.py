from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2, default=39.9)
    image = models.ImageField(upload_to='products', blank=True, null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None