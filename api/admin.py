from django.contrib import admin

# Register your models here.
from .models import (
    Category,
    Product,
    Marca,
    Cupon
)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Marca)
admin.site.register(Cupon)