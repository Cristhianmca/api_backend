from rest_framework import generics
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
import mercadopago
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from rest_framework.generics import RetrieveAPIView



from .models import Cupon  





from .models import (
    Category,Product,
    Client,Order,
    PaymentMethod,
    OrderPayment,
    Marca,
    Cupon
)

from .serializers import (
    CategorySerializer,
    ProductSerializer,
    CategoryProductSerializer,
    ClientSerializer,
    UserSerializer,
    UserUpdateSerializer,
    ClientFullSerializer,
    OrderSerializer,
    PaymentMethodSerializer,
    OrderPaymentSerializer,
    MarcaSerializer,
    CuponSerializer
    
)

from django.contrib.auth.models import User


class CuponView(RetrieveAPIView):# se crea una clase para la vista de los cupones # se importa RetrieveAPIView que significa que se puede ver un solo objeto esto se hace para que se pueda ver un solo cupon y no todos los cupones en la base de datos 
    queryset = Cupon.objects.all()# se hace una consulta a la base de datos para que se pueda ver todos los cupones # se importa el modelo Cupon para que se pueda hacer la consulta a la base de datos # queryset es una variable que se usa para hacer la consulta a la base de datos # obejcts.all() se usa para que se pueda ver todos los cupones en la base de datos
    serializer_class = CuponSerializer #serializer_class es una variable que se usa para que se pueda serializar los datos de la base de datos # se importa CuponSerializer para que se pueda serializar los datos de la base de datos # serealizar es convertir los datos de la base de datos en un formato que se pueda ver en la pagina web
    lookup_field = 'codigo'# se crea una variable que se llama lookup_field que se usa para que se pueda buscar un cupon por el codigo # se pone codigo porque es el campo que se va a usar para buscar un cupon en la base de datos
    

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class MarcaView(generics.ListAPIView): # se crea una clase para la vista de las marcas # se importa ListAPIView que significa que se puede ver una lista de objetos esto se hace para que se pueda ver una lista de marcas y no una sola marca en la base de datos
    queryset = Marca.objects.all()# se hace una consulta a la base de datos para que se pueda ver todas las marcas # se importa el modelo Marca para que se pueda hacer la consulta a la base de datos # queryset es una variable que se usa para hacer la consulta a la base de datos # obejcts.all() se usa para que se pueda ver todas las marcas en la base de datos
    serializer_class = MarcaSerializer#serializer_class es una variable que se usa para que se pueda serializar los datos de la base de datos # se importa MarcaSerializer para que se pueda serializar los datos de la base de datos # serealizar es convertir los datos de la base de datos en un formato que se pueda ver en la pagina web
    
class MarcaDetailView(generics.RetrieveAPIView):# se crea una clase para la vista de una marca # se importa RetrieveAPIView que significa que se puede ver un solo objeto esto se hace para que se pueda ver una sola marca y no todas las marcas en la base de datos #generic.RetrieveAPIView se usa para que se pueda ver un solo objeto en la base de datos
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    

class ProductView(generics.ListAPIView):# se crea una clase para la vista de los productos # se importa ListAPIView que significa que se puede ver una lista de objetos esto se hace para que se pueda ver una lista de productos y no un solo producto en la base de datos
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):# se crea una clase para la vista de un producto # se importa RetrieveAPIView que significa que se puede ver un solo objeto esto se hace para que se pueda ver un solo producto y no todos los productos en la base de datos #generic.RetrieveAPIView se usa para que se pueda ver un solo objeto en la base de datos , se puede buscar un producto por el id
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryProductsView(generics.RetrieveAPIView):# se crea una clase para la vista de los productos de una categoria # se importa RetrieveAPIView que significa que se puede ver un solo objeto esto se hace para que se pueda ver un solo producto y no todos los productos en la base de datos #generic.RetrieveAPIView se usa para que se pueda ver un solo objeto en la base de datos
    queryset = Category.objects.all()# se hace una consulta a la base de datos para que se pueda ver todas las categorias # se importa el modelo Category para que se pueda hacer la consulta a la base de datos # queryset es una variable que se usa para hacer la consulta a la base de datos # obejcts.all() se usa para que se pueda ver todas las categorias en la base de datos
    lookup_url_kwarg = 'category_id'# se crea una variable que se llama lookup_url_kwarg que se usa para que se pueda buscar una categoria por el id # se pone category_id porque es el campo que se va a usar para buscar una categoria en la base de datos
    serializer_class = CategoryProductSerializer

class ClientView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClienteDetailView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClienteDetailByUserView(generics.RetrieveAPIView):
    serializer_class = ClientSerializer

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        user = User.objects.get(pk=user_id)

        client = Client.objects.filter(user=user).first()

        return client

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

class ClientDetailFullView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientFullSerializer

class ClientFullView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientFullSerializer

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class PaymentMethodView(generics.ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class OrderPaymentView(generics.ListCreateAPIView):
    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer
    
class CreatePaymentView(APIView):# se crea una clase para la vista de los pagos # se importa APIView que significa que se puede hacer una solicitud a la base de datos esto se hace para que se pueda hacer una solicitud a la base de datos para que se pueda hacer un pago en la pagina web #generic.RetrieveAPIView se usa para que se pueda hacer una solicitud a la base de datos
    def post(self, request):
        # Obtener los productos desde la base de datos
        products = Product.objects.all() # Obtener todos los productos
        
        
        
     
    

        # Crear una lista de ítems para la preferencia de pago
        items = []# se crea una lista que se llama items que se usa para que se pueda guardar los productos que se van a comprar en la pagina web # se pone items porque es el nombre de la lista que se va a usar para guardar los productos que se van a comprar en la pagina web # si le asigno un nombre diferente no se va a guardar los productos que se van a comprar en la pagina web
        
        for product in products: 
            # Recorrer todos los productos de la base de datos # se crea un bucle que se llama product que se usa para que se pueda recorrer todos los productos de la base de datos # se pone product porque es el nombre del bucle que se va a usar para recorrer todos los productos de la base de datos # si le asigno un nombre diferente no se va a recorrer todos los productos de la base de datos
            
            
            item = {# se crea una variable que se llama item que se usa para que se pueda guardar los productos que se van a comprar en la pagina web # se pone item porque es el nombre de la variable que se va a usar para guardar los productos que se van a comprar en la pagina web # si le asigno un nombre diferente no se va a guardar los productos que se van a comprar en la pagina web
               
                "id": product.id,  # aqui va el id del producto de la base de datos # se pone id porque es el campo que se va a usar para guardar el id del producto de la base de datos # si le asigno un nombre diferente no se va a guardar el id del producto de la base de datos
                "title": product ,  # Nombre del producto
                "quantity": 1 ,  # Cantidad del producto si pongo 1 es porque solo se va a comprar un producto # si quiero que se pueda comprar mas de un producto solo tengo que cambiar el numero a la cantidad de productos que se quiera comprar pero si quiero por defecto que se almace los productos que se van a comprar en la pagina web solo tengo que poner 1
                "currency_id": "PEN",  # Moneda (Soles)
                "unit_price": float(product.price)  # Precio del producto # float se usa para que se pueda guardar el precio del producto en la pagina web # si no se pone float no se va a guardar el precio del producto en la pagina web
                
                
            }
            items.append(item)# se usa append para que se pueda guardar los productos que se van a comprar en la pagina web # si no se pone append no se va a guardar los productos que se van a comprar en la pagina web

        # Construir la preferencia de pago con los ítems
        preference_data = {# se crea una variable que se llama preference_data que se usa para que se pueda guardar los productos que se van a comprar en la pagina web # se pone preference_data porque es el nombre de la variable que se va a usar para guardar los productos que se van a comprar en la pagina web # si le asigno un nombre diferente no se va a guardar los productos que se van a comprar en la pagina web
            "items": items
        }

        # Hacer una solicitud a la API de Mercado Pago para crear la preferencia
        response = requests.post(# se hace una solicitud a la base de datos para que se pueda crear la preferencia de pago en la pagina web # se importa requests para que se pueda hacer una solicitud a la base de datos # se pone post porque se va a hacer una solicitud a la base de datos
            "https://api.mercadopago.com/checkout/preferences",# se pone la url de la base de datos para que se pueda hacer una solicitud a la base de datos # se pone la url de la base de datos para que se pueda crear la preferencia de pago en la pagina web # se pone la url de la base de datos para que se pueda hacer un pago en la pagina web
            json=preference_data,# se pone preference_data porque es la variable que se va a usar para guardar los productos que se van a comprar en la pagina web # si le asigno un nombre diferente no se va a guardar los productos que se van a comprar en la pagina web
            headers={
                "Authorization": "Bearer TEST-1403528576089699-040215-935134bd444d98cf740d4fb543844023-1724625949"
            }
            
            
        )

        if response.status_code == 201:
            preference_id = response.json().get("id")
            # Obtener el sandbox_init_point de la respuesta y devolverlo como parte de la respuesta
            init_point = response.json().get("init_point")
            return Response({"preference_id": preference_id, "init_point": init_point})
        else:
            # Manejo de errores
            return Response({"error": "No se pudo crear la preferencia de pago"}, status=response.status_code)

# class CreatePaymentView(APIView):
#     def post(self, request):
#         # Lógica para crear una preferencia de pago en Mercado Pago
#         # Aquí se incluirían los detalles del pago, como el monto, la descripción, etc.
#         preference_data = {
#             "items": [
#                 {
#                     "title": "Producto de prueba",
#                     "quantity": 1,
#                     "currency_id": "PEN",  # Moneda (Soles)
#                     "unit_price": 10.0  # Precio del producto
#                 }
#             ]
#         }

#         # Hacer una solicitud a la API de Mercado Pago para crear la preferencia
#         response = requests.post(
#             "https://api.mercadopago.com/checkout/preferences",
#             json=preference_data,
#             headers={
#                 "Authorization": "Bearer TEST-1403528576089699-040215-935134bd444d98cf740d4fb543844023-1724625949"
#     }
# )

#         if response.status_code == 200:
#             preference_id = response.json().get("id")
#             return Response({"preference_id": preference_id})
#         else:
#             # Imprimir la respuesta completa de la API
#             print(response.json())
#             # Manejo de errores
#             return Response({"error": "No se pudo crear la preferencia de pago"}, status=response.status_code)
# class CreatePaymentView(APIView):
#     def post(self, request):
#         try:
#             sdk = mercadopago.SDK("TEST-1403528576089699-040215-935134bd444d98cf740d4fb543844023-1724625949")

#             # Verifica si la solicitud contiene los datos esperados
#             if 'products' not in request.data or not isinstance(request.data['products'], list):
#                 return Response({'error': 'Datos de productos no encontrados o no válidos'}, status=400)

#             preference_data = {
#                 "items": [
#                     {
#                         "title": product.get('name', ''),  # Nombre del producto
#                         "currency_id": "PEN",  # Moneda en la que se realizará la transacción
#                         "unit_price": product.get('price', 0)  # Precio unitario del producto
#                     }
#                     for product in request.data['products']
#                 ]
#             }

#             preference_result = sdk.preference().create(preference_data)
#             if preference_result['status'] == 200 or preference_result['status'] == 201:
#                 payment_url = preference_result['response']['init_point']
#                 return Response({'payment_url': payment_url})
#             else:
#                 error_message = preference_result.get('message', 'Error desconocido al crear la preferencia de pago')
#                 print("Error creating payment preference: ", error_message)
#                 return Response({'error': error_message}, status=400)
#         except Exception as e:
#             print("Error en el servidor:", str(e))
#             return Response({'error': 'Error interno en el servidor'}, status=500)
    
# class CreatePaymentView(APIView):
#     def post(self, request):
#         sdk = mercadopago.SDK("TEST-1403528576089699-040215-935134bd444d98cf740d4fb543844023-1724625949")
        
#         # Aquí debes construir el objeto de preferencia de pago con los detalles de los productos y enviar la solicitud a Mercado Pago
#         preference_data = {
#             "items": [
#                 {
#                     "title": product['name'],  # Nombre del producto
#                     "currency_id": "PEN",  # Moneda en la que se realizará la transacción
#                     "unit_price": product['price']  # Precio unitario del producto
#                 }
#                 for product in request.data['products']
#             ]
#         }
        
#         preference_result = sdk.preference().create(preference_data)
#         if preference_result['status'] == 200 or preference_result['status'] == 201:
#             payment_url = preference_result['response']['init_point']
#             return Response({'payment_url': payment_url})
#         else:
#             print("Error creating payment preference: ", preference_result)
#             return Response({'error': 'Error al crear preferencia de pago'}, status=400)

# class CreatePaymentView(APIView):
#     def post(self, request):
#         sdk = mercadopago.SDK("TEST-1403528576089699-040215-935134bd444d98cf740d4fb543844023-1724625949")
#         preference_data = {
#             "items": [
#                 {
#                     "name": "Test Product",
#                     "quantity": 1,
#                     "currency_id": "PEN",
#                     "unit_price": 100.0
#                 }
#             ]
#         }


#         preference_result = sdk.preference().create(preference_data)
#         if preference_result['status'] == 200 or preference_result['status'] == 201:
#             payment_url = preference_result['response']['init_point']
#             return HttpResponseRedirect(payment_url)
#         else:
#             print("Error creating payment preference: ", preference_result)
#             return Response({'error': 'Error al crear preferencia de pago'}, status=400)
    #     payment_url = None
    #     if preference_result is not None and 'response' in preference_result and 'init_point' in preference_result['response']:
    #         payment_url = preference_result['response']['init_point']
    #     else:
    # # Handle the error
    #         print("Error creating payment preference: ", preference_result)
    #         return Response({'error': 'Error al crear preferencia de pago'}, status=400)



    def get(self, request):
        sdk = mercadopago.SDK("TEST-1403528576089699-040215-935134bd444d98cf740d4fb543844023-1724625949")
        search_result = sdk.payment().search({})
        if 'response' in search_result:
            return Response(search_result['response'])
        else:
            return Response({'error': 'No hay respuesta en el resultado'}, status=400)

