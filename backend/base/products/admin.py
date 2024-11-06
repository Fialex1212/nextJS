from django.contrib import admin
from .models import (
    PromoCode,
    Category,
    Size,
    Color, 
    Product
)

admin.site.register(PromoCode)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Product)
