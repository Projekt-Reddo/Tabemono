from django.db import models
from django.contrib.auth.models import User

# # Create your models here.

# Model Customers
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    CustomerID = models.CharField(max_length=8, null=False, blank=False, primary_key=True)
    CustomerName = models.CharField(max_length=50,null=False ,blank=True, unique=False)
    CustomerPhone = models.CharField(max_length=10, null=False, blank=False, unique=True)
    Email = models.CharField(max_length=100, null=False, blank=False, unique=True) 
    CustomerAddress = models.CharField(max_length=255, null=False, blank=True)
    UserName = models.CharField(max_length=32, null=False, blank=False, unique=True)
    Password = models.CharField(max_length=32, null=False, blank=False)
    DateOfBirth = models.DateTimeField(default='1900/01/01')
    Gender = models.CharField(max_length=1, default='F')
    def __str__(self):
        return self.UserName

# Model Foods
class Food(models.Model):
    # Add Rating(Avg)(Like), Image, 
    FoodID = models.CharField(max_length=8, null=False, primary_key=True)
    FoodName = models.CharField(max_length=100, null=False, )
    Price = models.FloatField(null=False)
    Description = models.TextField(null=True, blank=True)
    Rating = models.FloatField()
    Img = models.ImageField(upload_to='images')
    def __str__(self):
        return self.FoodID

# Model Restaurants
class Restaurant(models.Model):
    RestaurantID = models.CharField(max_length=8, null=False, primary_key=True)
    RestaurantName = models.CharField(max_length=50, null=False, blank=True)
    RestaurantAddress = models.CharField(max_length=255, null=False, blank=True)
    RestaurantPhone = models.CharField(max_length=10, null=False, blank=False)
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
        ShipperID = models.CharField(max_length=8, null=False, blank=False, primary_key=True)
        ShipperName = models.CharField(max_length=50, null=False, blank=True)
        ShipperPhone = models.CharField(max_length=10, null=False, blank=False)
        ShipperStatus = models.BooleanField(default=False)
        def __str__(self):
            return self.ShipperID

# Model Payments
    class Payment(models.Model):
        PaymentID = models.AutoField(primary_key=True)
        PaymentMethod = models.CharField(max_length=50, null=False, blank=True)
        def __str__(self):
            return self.PaymentID

# Model Orders
    class Order(models.Model):
        OrderID =models.Model(max_length=8, null=False, blank=False, primary_key=True)
        CustomerID= models.ForeignKey(Customer.CustomerID, on_delete=models.CASCADE)
        ShipperID= models.ForeignKey('Shipper', on_delete=models.CASCADE)
        PaymentID= models.ForeignKey('Payment', on_delete=models.CASCADE)
        OrderDate = models.DateTimeField(null=False)
        OrderStatus = models.IntegerField(max_length=1, default=0)

# Model Orders Detail
    class OrderDetail(models.Model):
        OrderID = models.ForeignKey('Order', on_delete=models.CASCADE)
        FoodID = models.ForeignKey('Food', on_delete=models.CASCADE)
        Quantity = models.IntegerField(default=1)


# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     username = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.TextField()
    
#     gender = models.CharField(max_length=10)
#     dateOfBirth = models.DateTimeField()
#     is_shipper = models.BooleanField(default=False)
#     def str(self):
#         return self.username

# # class Food(models.Model):
# #     # Add Rating(Avg)(Like), Image, 
# #     food_name = models.CharField(max_length=100, null=True)
# #     price = models.FloatField()
# #     rating = models.FloatField()
# #     img = models.ImageField(upload_to='images')
# #     def str(self):
# #         return self.food_name

# # # Food in cart
# # class Order(models.Model):
# #     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
# #     date_order = models.DateTimeField(auto_now_add=True)
# #     complete = models.BooleanField(default=False)
# #     transaction_id = models.CharField(max_length=100)

# # # Food is added to cart
# # class OrderFood(models.Model):
# #     food_id = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
# #     order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
# #     quantity = models.IntegerField(default=0)
# #     date_add = models.DateTimeField(auto_now_add=True)

# # # Ship
# # class Shipping(models.Model):
# #     food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
# #     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
# #     address = models.CharField(max_length=100)
# #     zip_code = models.CharField(max_length=100)
# #     date_add = models.DateTimeField(auto_now_add=True)
# #     def __str__(self):
# #         return self.address
