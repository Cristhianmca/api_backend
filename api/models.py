from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'tbl_category'
    
    def __str__(self):
        return self.name
    
class Marca(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'tbl_marca'
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    # aqui marca significa la marca del producto y que se relaciona con la tabla Marca 
    marca = models.ForeignKey(Marca,
                          related_name='products',
                          on_delete=models.RESTRICT,
                          default=1)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=0, )
    
    
    image = CloudinaryField('image',default='')
    
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.RESTRICT)
   
    class Meta:
        db_table = 'tbl_product'
    
    def __str__(self):
        return self.name
    
class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.RESTRICT)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    
    class Meta:
        db_table = 'tbl_client'
        
    def __str__(self):
        return self.user.username
    
class Order(models.Model):
    
    STATUS_CHOICES = (
        ('1','pending'),
        ('2','complete')
    )
    
    code = models.CharField(max_length=10)
    register_date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client,on_delete=models.RESTRICT)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    discount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='1')
    
    class Meta:
        db_table = 'tbl_order'
    
    def __str__(self):
        return self.code
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,
                              related_name='details',
                              on_delete=models.RESTRICT)
    product = models.ForeignKey(Product,
                                on_delete=models.RESTRICT)
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    
    class Meta:
        db_table = 'tbl_order_detail'
        
    def __str__(self):
        return self.product.name
    
class PaymentMethod(models.Model):
    name = models.CharField(max_length=200)
    account_email = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'tbl_payment_method'
        
    def __str__(self):
        return self.name
    
class OrderPayment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.RESTRICT)
    payment_method = models.ForeignKey(PaymentMethod,on_delete=models.RESTRICT)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    refer_number = models.TextField()
    
    class Meta:
        db_table = 'tbl_order_payment'
        
    def __str__(self):
        return self.order.code
    