from django.urls import path
from appentrega import views

urlpatterns = [
    path('', views.inicio),
    path('empleados/', views.empleados, name="Empleados"),
    path('trabajos/', views.trabajos, name="Trabajos"),
    path('empresas/', views.empresas, name="Empresas"),
    path('form-empleados/', views.form_empleados, name="FormEmpleado"),
]

