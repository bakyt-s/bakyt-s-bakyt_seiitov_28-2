from django.db import models


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    rate = models.FloatField(default=0)
    article = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=256)
    created_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.title} - {self.text}'
