from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('de-scripts/', views.index_de_scripts, name='bases_des'),
    path('cake/', views.cake, name='cakes'),
    path('cake/de-scripts/', views.cake_de_scripts, name='cakes_des'),
    path('cupcake/', views.cupcake, name='cupcakes'),
    path('cupcake/de-scripts/', views.cake_de_scripts, name='cupcakes_des'),
]