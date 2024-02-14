from django.shortcuts import render, redirect
from appentrega.models import Empleado
# Create your views here.

def inicio(request):
    return render(request, "appentrega/index.html")

def empleados(request):
    return render(request, "appentrega/empleados.html")

def trabajos(request):
    return render(request, "appentrega/trabajos.html")

def empresas(request):
    return render(request, "appentrega/empresas.html")

def form_empleados(request):
      
      if request.method == 'POST':

        empleado = Empleado(nombre=request.POST['nombre'],apellido=request.POST['apellido'],trabajo=request.POST['trabajo'])
 
        empleado.save()
 
        return render(request, "appentrega/index.html")
 
      return render(request,"appentrega/form_empleados.html")

