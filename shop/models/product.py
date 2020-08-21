from django.db import models

from shop.helpers import upload_path, generate_random_name
from shop.models.category import Category


class ProductActiveManager(models.Manager):
    def get_queryset(self):
        """
        Return active products
        :return:
        """
        return super(ProductActiveManager, self).get_queryset().\
            filter( active=True )


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, db_index=True, blank=True)
    image = models.ImageField(upload_to=upload_path)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def save(self, *args, **kwargs):
        """
        Modify the slug field to a random string and save
        :return:
        """
        self.slug = generate_random_name(self.name)

    objects = models.Manager()
    active = ProductActiveManager()

    def __str__(self):
        return self.name
