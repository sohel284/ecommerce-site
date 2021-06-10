from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=264, )
    created_at = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"

class Product(models.Model):
    category = models.ForeignKey(Category, models.CASCADE, related_name='category')
    product_image = models.ImageField(upload_to='product_pics')
    name = models.CharField(max_length=255, )
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    preview_details = models.TextField(max_length=1000, verbose_name='Preview Details')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return self.name  

    class Meta:
        ordering = ('-created_at', )
     


