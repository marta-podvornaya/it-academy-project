from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Item(models.Model):
    category_types = [('c',"Одежда"), ('u', "Нижнее белье"), ('j', "Бижутерия"), ('a', "Аксессуары")]

    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100, primary_key=True)
    category = models.CharField(choices=category_types, max_length=100)
    price = models.CharField(max_length=30)
    details = models.CharField(max_length=100)
    image = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    genders = [('f', "Женский"), ('m', "Мужской"), ('o', "Другое"), ('no', "Не хочу сообщать")]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(choices=genders, max_length=100, default="Не хочу сообщать")

    def __str__(self):
        return self.name


class Order(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=30)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        total = int(self.item.price) * self.quantity
        return total

    def __str__(self):
        return self.item

class Question(models.Model):

    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.EmailField(null=False)
    date = models.DateTimeField(auto_now_add=True)