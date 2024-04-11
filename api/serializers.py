from rest_framework import serializers

from django.contrib.auth.models import User

from .models import (
    Category,Product,
    Client,
    Order,OrderDetail,
    PaymentMethod,OrderPayment,
    Marca,
    Cupon,
)

class CuponSerializer(serializers.ModelSerializer):#serializador para el modelo Cupon
    class Meta:#clase Meta para definir el modelo y los campos a serializar
        model = Cupon
        fields = ['codigo', 'porcentaje_descuento', 'fecha_vencimiento', 'cantidad_usos', 'cantidad_usos_limite']#campos a serializar del modelo Cupon que significan el codigo, porcentaje de descuento, fecha de vencimiento, cantidad de usos, cantidad de usos limite

    
        
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        return representation
    
class MarcaSerializer(serializers.ModelSerializer):#serializador para el modelo Marca
    class Meta:#clase Meta para definir el modelo y los campos a serializar
        model = Marca #modelo Marca
        fields = '__all__' # todos los campos del modelo Marca
        
    def to_representation(self,instance): #metodo para representar los datos del modelo Marca en el serializador MarcaSerializer 
        representation = super().to_representation(instance) #se obtiene la representacion de la instancia del modelo Marca esto quiere decir que se obtienen todos los campos del modelo Marca
        representation['image'] = instance.image.url #se agrega el campo image a la representacion de la instancia del modelo Marca y se le asigna la url de la imagen de la instancia
        return representation
        
class ProductSerializer(serializers.ModelSerializer):#serializador para el modelo Product
    class Meta:
        model = Product
        fields = '__all__'
        
    def to_representation(self,instance):#metodo para representar los datos del modelo Product en el serializador ProductSerializer
        representation = super().to_representation(instance)#se obtiene la representacion de la instancia del modelo Product esto quiere decir que se obtienen todos los campos del modelo Product
        representation['image'] = instance.image.url #se agrega el campo image a la representacion de la instancia del modelo Product y se le asigna la url de la imagen de la instancia se le debe pasar el campo image de la instancia y se le debe asignar la url de la imagen de la instancia a diferencia de en models.py que se le asigna la imagen a la instancia esto quiere decir que se le asigna la url de la imagen a la representacion de la instancia , esta imagen se puede visualizar en el navegador en la url que se le asigno a la imagen
        return representation
    
class CategoryProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,read_only=True)
    
    class Meta:
        model = Category
        fields = ['id','name','products']
                
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        representation['fullname'] = instance.user.first_name + ' ' + instance.user.last_name
        representation['email'] = instance.user.email
        return representation
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        extra_kwargs = {'password':{'write_only':True}}
        
    def create(self,validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']
        
class UserFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        extra_kwargs = {'password':{'write_only':True}}
        
class ClientFullSerializer(serializers.ModelSerializer):
    user = UserFullSerializer()
    
    class Meta:
        model = Client
        fields = ('user','phone','address')
        
    def create(self,validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        client = Client.objects.create(user=user,**validated_data)
        return client
    
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('product','quantity','subtotal')
        
class OrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['code','register_date','client','total_price','discount','details']
        
    def create(self,validated_data):
        list_details = validated_data.pop('details')
        order = Order.objects.create(**validated_data)
        for obj_detail in list_details:
            OrderDetail.objects.create(order=order,**obj_detail)
        return order
    
class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        return representation
    
class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPayment
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        representation['payment_method_name'] = instance.payment_method.name #se agrega el campo payment_method_name a la representacion de la instancia del modelo OrderPayment y se le asigna el nombre del metodo de pago de la instancia
        return representation
        
        