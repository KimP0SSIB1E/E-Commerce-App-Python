from django.db import models
from django.conf import settings


# Create your models here.
<<<<<<< HEAD

class Collection(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
=======
class Product(models.Model):
    title = models.CharField(max_length =255, null=False, blank=False)
>>>>>>> fddd4f46c97da1ff325237857d7b4dd48b7c1931
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
<<<<<<< HEAD
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotion = models.ManyToManyField('Promotion', related_name='+')


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    PAYMENT_STATUS = [
        ('P', 'Pending'),
        ('S', 'Success'),
        ('F', 'Failed')

    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default='P')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Promotion(models.Model):
    promotion = models.ManyToManyField(Product, related_name='+')
    discount = models.DecimalField(max_digits=6, decimal_places=2)
=======

class Collection(models.Model):
    title = models.CharField(max_length=255)

class Cart(models.Model):
    title = models.CharField(max_length=255)

class CartItem(models.Model):
    cart =
    product =
    quantity =
>>>>>>> fddd4f46c97da1ff325237857d7b4dd48b7c1931
