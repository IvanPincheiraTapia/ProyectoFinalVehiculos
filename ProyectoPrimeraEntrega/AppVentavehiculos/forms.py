from socket import fromshare
from django import forms

class VehiculoFormulario(forms.Form):

    tipo = forms.CharField()
    marca = forms.CharField()
    modelo = forms.CharField()
    puertas = forms.IntegerField()
    usado = forms.CharField()
    kilometros = forms.IntegerField()
    año = forms.IntegerField()
    precio = forms.IntegerField()

class VendedorFormulario(forms.Form):

    nombre = forms.CharField()
    email = forms.CharField()
    telefono = forms.IntegerField()
    atencion = forms.CharField()

class SucursalesFormulario(forms.Form):

    nombre = forms.CharField()
    ubicacion = forms.CharField()
    telefono = forms.IntegerField()