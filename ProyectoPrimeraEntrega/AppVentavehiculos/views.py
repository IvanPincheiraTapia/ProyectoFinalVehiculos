from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import SucursalesFormulario, VehiculoFormulario, VendedorFormulario
from .models import vehiculo, sucursales, vendedor

# Create your views here.

def vehiculos(request):
    
    lista = vehiculo.objects.all()
    return render(request, "vehiculos.html", {"vehiculos": lista})

def sucursal(request):

    listasucursal = sucursales.objects.all()
    return render(request, "sucursales.html", {"sucursales": listasucursal})

def vendedores(request):

    listavendedores = vendedor.objects.all()
    return render(request, "vendedor.html", {"vendedor": listavendedores})

def inicio(request):

    return render(request, "inicio.html")

def formulario(request):

    if request.method == "POST":
        
        mi_formulario = VehiculoFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            objetos = vehiculo(tipo=data['tipo'], marca=data['marca'], modelo=data['modelo'], usado=data['usado'], 
            puertas=data['puertas'], kilometros=data['kilometros'], año=data['año'], precio=data['precio'])
            objetos.save()
            return redirect('vehiculos')
    else:
        mi_formulario =VehiculoFormulario()

    return render(request, 'Formulario.html', {'mi_formulario':mi_formulario})

def formulario_vendedor(request):

    if request.method == "POST":
        
        mi_formulariovendedor = VendedorFormulario(request.POST)
        if mi_formulariovendedor.is_valid():
            data = mi_formulariovendedor.cleaned_data
            objetos = vendedor(nombre=data['nombre'], email=data['email'], telefono=data['telefono'], atencion=data['atencion'])
            objetos.save()
            return redirect('vendedor')
    else:
        mi_formulariovendedor =VendedorFormulario()

    return render(request, 'Formulario_vendedor.html', {'mi_formulariovendedor':mi_formulariovendedor})

def formulario_sucursal(request):

    if request.method == "POST":
        
        mi_formulariosucursal = SucursalesFormulario(request.POST)
        if mi_formulariosucursal.is_valid():
            data = mi_formulariosucursal.cleaned_data
            objetos = sucursales(nombre=data['nombre'], ubicacion=data['ubicacion'], telefono=data['telefono'])
            objetos.save()
            return redirect('sucursales')
    else:
        mi_formulariosucursal =SucursalesFormulario()

    return render(request, 'Formulario_sucursal.html', {'mi_formulariosucursal':mi_formulariosucursal})

def contacto(request):

    return render(request, "contacto.html")

def agradecimiento(request):

    return render(request, "Agradecimiento.html")

def busqueda_vendedor(request):

    return render(request, "busqueda_vendedor.html")

def buscar(request):

    buscar_nombre = request.GET['nombre']

    telefono = vendedor.objects.get(nombre = buscar_nombre)

    return render(request, 'resultadobusqueda.html', {'telefono': telefono})