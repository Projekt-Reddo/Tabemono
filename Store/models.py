from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_code = models.CharField(primary_key=True, unique=True, max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNum = models.CharField(max_length=15)
    password = models.TextField()
    gender = models.CharField(max_length=10)
    dateOfBirth = models.DateTimeField()
    is_shipper = models.BooleanField(default=False)
    def __str__(self):
        return self.username

# Food
class Food(models.Model):
    # Add Rating(Avg)(Like), Image, 
    food_name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    rating = models.FloatField()
    img = models.ImageField(upload_to='images')
    def __str__(self):
        return self.food_name

# Food in cart
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)

# Food is added to cart
class OrderFood(models.Model):
    food_id = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_add = models.DateTimeField(auto_now_add=True)

# Ship
class Shipping(models.Model):
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    date_add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address