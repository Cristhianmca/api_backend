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
    name = models.CharField(max_length=200)#nombre de la marca #charfield es un campo de texto que se le puede asignar un maximo de caracteres que son 200 a diferencia de textfield que no tiene limite y richtextfield que es un campo de texto enriquecido por lo que se puede agregar imagenes, videos, etc
    image = CloudinaryField('image',default='')#imagen de la marca #cloudinaryfield es un campo de imagen que se le puede asignar un nombre y un valor por defecto en este caso se le asigna un valor por defecto de un string vacio porque no se le asigna ninguna imagen por defecto a la marca 
    
    class Meta: #meta es una clase que se utiliza para definir metadatos de la clase en este caso se define el nombre de la tabla de la base de datos que se va a crear con el nombre de la clase   
        db_table = 'tbl_marca' #se define el nombre de la tabla de la base de datos que se va a crear con el nombre de la clase 
    
    def __str__(self): #se define el metodo __str__ que se utiliza para retornar un string que se va a mostrar en la vista de administrador de django en este caso se retorna el nombre de la marca , #un str es un string que se utiliza para mostrar un texto en la vista de administrador de django
        return self.name #se retorna el nombre de la marca 

class Cupon(models.Model):#se crea una clase llamada Cupon que hereda de models.Model
    codigo = models.CharField(max_length=10, unique=True)#se crea un campo llamado codigo que es un campo de texto que se le puede asignar un maximo de caracteres que son 10 y se le asigna un valor unico #unique=True se utiliza para que el valor del campo sea unico en la base de datos es decir que no se puede repetir
    porcentaje_descuento = models.DecimalField(max_digits=5, decimal_places=2)#se crea un campo llamado porcentaje_descuento que es un campo de decimal que se le puede asignar un maximo de digitos que son 5 y un maximo de decimales que son 2 #este campo se utiliza para asignar el porcentaje de descuento que se va a aplicar al producto #DecimalField es un campo de decimal que se utiliza para almacenar numeros decimales
    fecha_vencimiento = models.DateField()#se crea un campo llamado fecha_vencimiento que es un campo de fecha #este campo se utiliza para asignar la fecha de vencimiento del cupon #DateField es un campo de fecha que se utiliza para almacenar fechas
    cantidad_usos = models.IntegerField(default=0) #se crea un campo llamado cantidad_usos que es un campo de entero que se le puede asignar un valor por defecto de 0 #este campo se utiliza para asignar la cantidad de veces que se ha utilizado el cupon #IntegerField es un campo de entero que se utiliza para almacenar numeros enteros #default=0 se utiliza para asignar un valor por defecto al campo
    cantidad_usos_limite = models.IntegerField(default=0)#se crea un campo llamado cantidad_usos_limite que es un campo de entero que se le puede asignar un valor por defecto de 0 #este campo se utiliza para asignar la cantidad de veces que se puede utilizar el cupon
    #IntegerField es un campo de entero que se utiliza para almacenar numeros enteros 
    #default=0 se utiliza para asignar un valor por defecto al campo
    

    def __str__(self):#se define el metodo __str__ que se utiliza para retornar un string que se va a mostrar en la vista de administrador de django en este caso se retorna el codigo del cupon , #un str es un string que se utiliza para mostrar un texto en la vista de administrador de django
        return self.codigo


class Product(models.Model):#se crea una clase llamada Product que hereda de models.Model
    name = models.CharField(max_length=200)
    # aqui marca significa la marca del producto y que se relaciona con la tabla Marca 
    marca = models.ForeignKey(Marca,#se crea un campo llamado marca que es una clave foranea que se relaciona con la tabla Marca #ForeignKey es un campo de clave foranea que se utiliza para relacionar dos tablas de la base de datos #Marca es la tabla con la que se relaciona el campo
                          related_name='products',#related_name se utiliza para asignar un nombre a la relacion entre las tablas #en este caso se le asigna el nombre de products a la relacion entre la tabla Product y la tabla Marca
                          on_delete=models.RESTRICT,#on_delete se utiliza para definir que accion se va a realizar cuando se elimine un registro de la tabla relacionada #en este caso se define que no se puede eliminar un registro de la tabla Marca si hay un registro de la tabla Product que esta relacionado con el registro de la tabla Marca
                          default=1)#default se utiliza para asignar un valor por defecto al campo #en este caso se le asigna un valor por defecto de 1 al campo #este campo se utiliza para asignar la marca del producto #un str es un string que se utiliza para mostrar un texto en la vista de administrador de django# se le asigno un valor por defecto de 1 porque no se puede asignar un valor nulo a un campo de clave foranea
    description = RichTextField()#se crea un campo llamado description que es un campo de texto enriquecido #este campo se utiliza para asignar la descripcion del producto #RichTextField es un campo de texto enriquecido que se utiliza para almacenar texto enriquecido
    specifications = RichTextField()#se crea un campo llamado specifications que es un campo de texto enriquecido #este campo se utiliza para asignar las especificaciones del producto #RichTextField es un campo de texto enriquecido que se utiliza para almacenar texto enriquecido
    
    price = models.DecimalField(max_digits=10, decimal_places=0, )#se crea un campo llamado price que es un campo de decimal que se le puede asignar un maximo de digitos que son 10 y un maximo de decimales que son 0 #este campo se utiliza para asignar el precio del producto #DecimalField es un campo de decimal que se utiliza para almacenar numeros decimales
    price_discount = models.DecimalField(max_digits=10, 
                                         decimal_places=0, default=0)#se crea un campo llamado price_discount que es un campo de decimal que se le puede asignar un maximo de digitos que son 10 y un maximo de decimales que son 0 y se le asigna un valor por defecto de 0 #este campo se utiliza para asignar el precio con descuento del producto #DecimalField es un campo de decimal que se utiliza para almacenar numeros decimales
    cupon = models.ForeignKey(Cupon, related_name='productos',#se crea un campo llamado cupon que es una clave foranea que se relaciona con la tabla Cupon #ForeignKey es un campo de clave foranea que se utiliza para relacionar dos tablas de la base de datos #Cupon es la tabla con la que se relaciona el campo #related_name se utiliza para asignar un nombre a la relacion entre las tablas #en este caso se le asigna el nombre de productos a la relacion entre la tabla Product y la tabla Cupon
                              on_delete=models.SET_NULL,#on_delete se utiliza para definir que accion se va a realizar cuando se elimine un registro de la tabla relacionada #en este caso se define que se va a asignar un valor nulo al campo si se elimina un registro de la tabla Cupon que esta relacionado con el registro de la tabla Product #SET_NULL se utiliza para asignar un valor nulo al campo
                              null=True, blank=True)#null se utiliza para definir si el campo puede tener un valor nulo #en este caso se define que el campo puede tener un valor nulo #blank se utiliza para definir si el campo puede estar vacio #en este caso se define que el campo puede estar vacio
    stock = models.IntegerField(default=0)#se crea un campo llamado stock que es un campo de entero que se le puede asignar un valor por defecto de 0 #este campo se utiliza para asignar la cantidad de productos que hay en stock #IntegerField es un campo de entero que se utiliza para almacenar numeros enteros #default=0 se utiliza para asignar un valor por defecto al campo
    available = models.BooleanField(default=True)#se crea un campo llamado available que es un campo de booleano que se le puede asignar un valor por defecto de True #este campo se utiliza para definir si el producto esta disponible o no #BooleanField es un campo de booleano que se utiliza para almacenar valores booleanos #default=True se utiliza para asignar un valor por defecto al campo # un booleano es un campo que se utiliza para almacenar valores de verdadero o falso
    
    image = CloudinaryField('image',default='')#se crea un campo llamado image que es un campo de imagen que se le puede asignar un nombre #CloudinaryField es un campo de imagen que se utiliza para almacenar imagenes #image es el nombre del campo #default='' se utiliza para asignar un valor por defecto al campo #en este caso se le asigna un valor por defecto de un string vacio porque no se le asigna ninguna imagen por defecto al producto
    
    category = models.ForeignKey(Category,#se crea un campo llamado category que es una clave foranea que se relaciona con la tabla Category #ForeignKey es un campo de clave foranea que se utiliza para relacionar dos tablas de la base de datos #Category es la tabla con la que se relaciona el campo
                                 related_name='products',#related_name se utiliza para asignar un nombre a la relacion entre las tablas #en este caso se le asigna el nombre de products a la relacion entre la tabla Product y la tabla Category
                                 on_delete=models.RESTRICT)#on_delete se utiliza para definir que accion se va a realizar cuando se elimine un registro de la tabla relacionada #en este caso se define que no se puede eliminar un registro de la tabla Category si hay un registro de la tabla Product que esta relacionado con el registro de la tabla Category
   
    class Meta:
        db_table = 'tbl_product'
    
    def __str__(self):#se define el metodo __str__ que se utiliza para retornar un string que se va a mostrar en la vista de administrador de django en este caso se retorna el nombre del producto , #un str es un string que se utiliza para mostrar un texto en la vista de administrador de django
        return self.name#se retorna el nombre del producto
    
    
    
class Client(models.Model):#se crea una clase llamada Client que hereda de models.Model
    user = models.OneToOneField(User,on_delete=models.RESTRICT)#se crea un campo llamado user que es una clave foranea que se relaciona con la tabla User #ForeignKey es un campo de clave foranea que se utiliza para relacionar dos tablas de la base de datos #User es la tabla con la que se relaciona el campo #OneToOneField se utiliza para definir una relacion uno a uno entre las tablas # relacion uno a uno significa que un registro de la tabla Client esta relacionado con un registro de la tabla User
    phone = models.CharField(max_length=100)#se crea un campo llamado phone que es un campo de texto que se le puede asignar un maximo de caracteres que son 100 #este campo se utiliza para asignar el numero de telefono del cliente
    address = models.TextField()#se crea un campo llamado address que es un campo de texto #este campo se utiliza para asignar la direccion del cliente #TextField es un campo de texto que se utiliza para almacenar texto
    
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
    
class OrderDetail(models.Model): #se crea una clase llamada OrderDetail que hereda de models.Model #esta clase se utiliza para definir los detalles de una orden
    order = models.ForeignKey(Order, #se crea un campo llamado order que es una clave foranea que se relaciona con la tabla Order #ForeignKey es un campo de clave foranea que se utiliza para relacionar dos tablas de la base de datos #Order es la tabla con la que se relaciona el campo #esta relacion se utiliza para definir que un registro de la tabla OrderDetail esta relacionado con un registro de la tabla Order
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
    