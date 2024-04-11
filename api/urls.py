from django.urls import path
from django.urls import path


from . import views

urlpatterns = [
    path('cupon/<str:codigo>', views.CuponView.as_view()),#ruta para el serializador CuponSerializer que recibe el codigo del cupon como parametro y retorna el cupon con ese codigo 
    path('categories', views.CategoryView.as_view()),
    path('products',views.ProductView.as_view()),
    path('product/<int:pk>',views.ProductDetailView.as_view()),#ruta para el serializador ProductSerializer que recibe el id del producto como parametro y retorna el producto con ese id # pk es el id del producto 
    path('marca',views.MarcaView.as_view()),#ruta para el serializador MarcaSerializer que retorna todas las marcas
    path('marca/<int:pk>',views.MarcaDetailView.as_view()),#ruta para el serializador MarcaSerializer que recibe el id de la marca como parametro y retorna la marca con ese id #pk es el id de la marca
    path('category/<int:category_id>/products',views.CategoryProductsView.as_view()),
    path('client',views.ClientView.as_view()),
    path('user',views.UserView.as_view()),
    path('user/<int:pk>',views.UserDetailView.as_view()),
    path('client/<int:pk>',views.ClienteDetailView.as_view()),
    path('client/full/<int:pk>',views.ClientDetailFullView.as_view()),
    path('client/full',views.ClientFullView.as_view()),
    path('client/byuser/<int:user_id>',views.ClienteDetailByUserView.as_view()),
    path('order',views.OrderView.as_view()),
    path('paymentmethod',views.PaymentMethodView.as_view()),
    path('order/payment',views.OrderPaymentView.as_view()),
    path('create-payment/',views.CreatePaymentView.as_view()),
]