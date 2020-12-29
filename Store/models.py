from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Model Customers
class Customer(models.Model):
    CustomerID = models.CharField(max_length=8, null=False, primary_key=True)
    CustomerName = models.CharField(max_length=50, null=False)
    CustomerPhone = models.CharField(max_length=10, null=False, unique=True)
    Email = models.CharField(max_length=100, null=False, unique=True) 
    CustomerAddress = models.CharField(max_length=255, null=False)
    UserName = models.CharField(max_length=32, null=False, unique=True)
    Password = models.CharField(max_length=32, null=False)
    DateOfBirth = models.DateTimeField(default='1900/01/01')
    Gender = models.CharField(max_length=1, default='F')
    def __str__(self):
        return self.UserName

# Model Foods
class Food(models.Model):
    FoodID = models.CharField(max_length=8, null=False, primary_key=True)
    FoodName = models.CharField(max_length=100)
    Price = models.FloatField()
    Description = models.TextField(null=True)
    Rating = models.FloatField()
    Img = models.ImageField(upload_to='images')
    def __str__(self):
        return self.FoodID

# Model Restaurants
class Restaurant(models.Model):
    RestaurantID = models.CharField(max_length=8, null=False, primary_key=True)
    RestaurantName = models.CharField(max_length=50)
    RestaurantAddress = models.CharField(max_length=255, null=False)
    RestaurantPhone = models.CharField(max_length=10, null=False)
    BusinessHour = models.CharField(max_length=255, null=False, default='00:00 - 00:00')
    def __str__(self):
        return self.RestaurantID

# Model Serves
    class Serve(models.Model):
        FoodID = models.ForeignKey('Food', on_delete=models.CASCADE)
        RestaurantID = models.ForeignKey('Restaurant', on_delete=models.CASCADE )
        Discount = models.FloatField(default=0)
        def __str__(self):
            return self.Discount

# Model Shippers
    class Shipper(models.Model):
        ShipperID = models.CharField(max_length=8, null=False, primary_key=True)
        ShipperName = models.CharField(max_length=50, null=False)
        ShipperPhone = models.CharField(max_length=10, null=False)
        ShipperStatus = models.BooleanField(default=False)
        def __str__(self):
            return self.ShipperID

# Model Payments
    class Payment(models.Model):
        PaymentID = models.AutoField(primary_key=True)
        PaymentMethod = models.CharField(max_length=50, null=False)
        def __str__(self):
            return self.PaymentID

# Model Orders
    class Order(models.Model):
        OrderID = models.CharField(max_length=8, null=False, primary_key=True)
        CustomerID = models.ForeignKey('Customer', on_delete=models.CASCADE)
        ShipperID = models.ForeignKey('Shipper', on_delete=models.CASCADE)
        PaymentID = models.ForeignKey('Payment', on_delete=models.CASCADE)
        OrderDate = models.DateTimeField(auto_now_add=True)
        OrderStatus = models.IntegerField(default=0)
        def __str__(self):
            return self.OrderID

# Model Orders Detail
    class OrderDetail(models.Model):
        OrderID = models.ForeignKey('Order', on_delete=models.CASCADE)
        FoodID = models.ForeignKey('Food', on_delete=models.CASCADE)
        Quantity = models.IntegerField(default=1)
        def __str__(self):
            return self.Quantity

