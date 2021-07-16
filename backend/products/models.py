from django.db import models
from slugify import slugify
from mptt.models import TreeForeignKey
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.PositiveSmallIntegerField()
    main_image = models.ImageField(upload_to="products/", blank=True)
    eavs = models.ManyToManyField("Eav")
    category = TreeForeignKey(Category, null=True, blank=True, related_name="products", on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["price"]


class ProductAttribute(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductAttribute, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductAttributeValue, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Eav(models.Model):
    attribute = models.ForeignKey("ProductAttribute", on_delete=models.CASCADE)
    values = models.ManyToManyField("ProductAttributeValue")
