from django.contrib import admin
from django.urls import path

from .views import agradecimiento, buscar, busqueda_vendedor, contacto, formulario, formulario_sucursal, inicio, sucursal, vehiculos, vendedores, formulario_vendedor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehiculos/', vehiculos, name="vehiculos"),
    path('vendedor/', vendedores, name="vendedor"),
    path('sucursales/', sucursal, name="sucursales"),
    path('inicio/', inicio, name="inicio"),
    path('Formulario/', formulario, name="Formulario"),
    path('contacto/', contacto, name="contacto"),
    path('agradecimiento/', agradecimiento, name="Agradecimiento"),
    path('busqueda_vendedor/', busqueda_vendedor, name="busqueda_vendedor"),
    path('buscar/', buscar, name="busqueda"),
    path('Formulario_vendedor/', formulario_vendedor, name="Formulario_vendedor"),
    path('Formulario_sucursal/', formulario_sucursal, name="Formulario_sucursal"),
]