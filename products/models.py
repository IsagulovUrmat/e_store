from django.db import models

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

    def __str__(self):
        return f"{self.name} {self.type} {self.price}"


class Order(models.Model):
    statuses = (
        ('In Process', 'In Process'),
        ('Delivered', 'Delivered'),
        ('Not Delivered', 'Not Delivered')
    )
    products = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=statuses, default='In Process')
    date_created = models.DateTimeField(auto_now_add=True)

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









