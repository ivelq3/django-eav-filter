from django.db import models
from slugify import slugify


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
