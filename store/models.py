from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=20 )


# collecting all categories
    @staticmethod
    def get_all_category():
        return Category.objects.all()

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.CharField(max_length=200 , default='')
    image = models.ImageField(upload_to='uploads/products/')
    
    @staticmethod
    def get_products_by_ids(ids):
        return Product.objects.filter(id__in=ids)   #to get products for multiple ids
# methods to get data of €products
    @staticmethod
    def get_all_products():
        return Product.objects.all() 
    @staticmethod
    def get_all_products_by_Id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id) 
        else:
            return Product.get_all_products()


class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone =models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_custome_by_email(email):
        return Customer.objects.get(email=email)

    def isEmailExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    address = models.CharField(max_length=200,default=" ")
    price = models.IntegerField(default=0)
    mobile = models.CharField(max_length=10,default=0)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer_id(cusotmer_id):
        return Order.objects.filter(customer = cusotmer_id).order_by('-date')
    





