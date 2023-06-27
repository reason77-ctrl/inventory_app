from django.db import models
from django.urls import reverse

# STATUS = (
#     ('active','active'),
#     ('inactive','inactive'),
# )


class Category(models.Model):
    title = models.CharField('Category Name', max_length=100)
    fa_image = models.CharField('Fas Fa Image',max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(upload_to="media/product_img")
    title = models.CharField('Product Name',max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    date_field = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
