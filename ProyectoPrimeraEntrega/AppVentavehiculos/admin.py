from atexit import register
from django.contrib import admin

from AppVentavehiculos.models import sucursales, vehiculo, vendedor

# Register your models here.

admin.site.register(vehiculo)
admin.site.register(vendedor)
admin.site.register(sucursales) 