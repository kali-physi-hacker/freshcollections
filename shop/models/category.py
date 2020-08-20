from django.db import models

from shop.helpers import upload_path, generate_random_name


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to=upload_path)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        """
        Modify the slug field to a random name containing the category's name
        and save
        :param args:
        :param kwargs:
        :return:
        """
        random_name = generate_random_name(self.name)
        self.slug = random_name
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
