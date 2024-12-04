from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    product_prie = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    image = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.product_prie)
    
   


