from rest_framework import generics
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
import mercadopago



from .models import (
    Category,Product,
    Client,Order,
    PaymentMethod,
    OrderPayment
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
    OrderPaymentSerializer
)

from django.contrib.auth.models import User

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ProductView(generics.ListAPIView):
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
        sdk = mercadopago.SDK("TEST-1403528576089699-040215-935134bd444d98cf740d4fb543844023-1724625949")
        preference_data = {
            "items": [
                {
                    "title": "My Item",
                    "quantity": 1,
                    "currency_id": "PEN",
                    "unit_price": 100.0
                }
            ]
        }
        
        
        preference_result = sdk.preference().create(preference_data)
        if preference_result['status'] == 200 or preference_result['status'] == 201:
            payment_url = preference_result['response']['init_point']
            return HttpResponseRedirect(payment_url)
        else:
            print("Error creating payment preference: ", preference_result)
            return Response({'error': 'Error al crear preferencia de pago'}, status=400)
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
    
    