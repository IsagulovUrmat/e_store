from django.contrib.auth.models import User
from django.db import models
from datetime import date

# Create your models here.

class Products(models.Model):
    type_of_product = (
        ('Laptop', 'Laptop'),
        ('PC', 'PC'),
        ('Mobile', 'Mobile')

    )
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, default="default_image.jpg")
    description = models.TextField()
    type = models.CharField(choices=type_of_product, max_length=20)
    price = models.IntegerField(blank=True,null=True)
    sale = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.type} {self.price}"


class Order(models.Model):
    statuses = (
        ('In Process', 'In Process'),
        ('Delivered', 'Delivered'),
        ('Not Delivered', 'Not Delivered')
    )
    p_methods = (
        ('money', 'money'),
        ('wallet', 'wallet')
    )
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    products = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=statuses, default='In Process')
    date_created = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=p_methods)


    def __str__(self):
        return f"{self.products} {self.quantity}"

class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

class Contacts(models.Model):
    type_of = (
        ('Email', 'Email'),
        ('Phone number', 'Phone number'),
    )
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phy_adress = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=type_of, default=phonenumber)
    latitude = models.IntegerField(blank=True, null=True)
    longtitude = models.IntegerField(blank=True, null=True)

class Profile(models.Model):
    genders = (
        ('F', 'F'),
        ('M', 'M')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, default="defaul_image.png")
    full_name = models.CharField(max_length=50)
    gender = models.CharField(choices=genders, max_length=20)
    description = models.TextField()
    birth_date = models.DateField(default=date.today())
    twitter_link = models.CharField(max_length=50)
    order_count = models.PositiveIntegerField(default=0)
    wallet = models.PositiveIntegerField(default=0)
    sale_amount = models.FloatField(default=0.1)

    def __str__(self):
        return f"{self.user}"










