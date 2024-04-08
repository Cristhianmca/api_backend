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




from .models import (
    Category,Product,
    Client,Order,
    PaymentMethod,
    OrderPayment,
    Marca
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
    MarcaSerializer
)

from django.contrib.auth.models import User

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class MarcaView(generics.ListAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    
class MarcaDetailView(generics.RetrieveAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    

class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryProductsView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    lookup_url_kwarg = 'category_id'
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
    
class CreatePaymentView(APIView):
    def post(self, request):
        # Obtener los productos desde la base de datos
        products = Product.objects.all() # Obtener todos los productos
        
     
    

        # Crear una lista de ítems para la preferencia de pago
        items = []
        
        for product in products:
            
            item = {
                
                "id": product.id,  # ID del producto, puede ser cualquier valor único
                "title": product.name,  # Nombre del producto
                "quantity": 1,  # Cantidad del producto (puedes ajustarlo según tu lógica)
                "currency_id": "PEN",  # Moneda (Soles)
                "unit_price": float(product.price)  # Precio del producto
                
                
            }
            items.append(item)

        # Construir la preferencia de pago con los ítems
        preference_data = {
            "items": items
        }

        # Hacer una solicitud a la API de Mercado Pago para crear la preferencia
        response = requests.post(
            "https://api.mercadopago.com/checkout/preferences",
            json=preference_data,
            headers={
                "Authorization": "Bearer TEST-1403528576089699-040215-935134bd444d98cf740d4fb543844023-1724625949"
            }
        )

        if response.status_code == 201:
            preference_id = response.json().get("id")
            # Obtener el sandbox_init_point de la respuesta y devolverlo como parte de la respuesta
            sandbox_init_point = response.json().get("sandbox_init_point")
            return Response({"preference_id": preference_id, "sandbox_init_point": sandbox_init_point})
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

