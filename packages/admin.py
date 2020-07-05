from django.contrib import admin
from .models import Cake, CupCake, Product

admin.site.register(Product)
admin.site.register(Cake)
admin.site.register(CupCake)
