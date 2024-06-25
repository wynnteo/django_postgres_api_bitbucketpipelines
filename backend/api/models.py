from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    store_id = models.CharField(max_length=255)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_dt = models.DateTimeField(auto_now_add=True)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    status_choices = [
        ('CREATED', 'Created'),
        ('PAID', 'Paid'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='CREATED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)