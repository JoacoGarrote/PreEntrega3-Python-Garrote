from django.urls import path
from appentrega import views

urlpatterns = [
    path('', views.inicio),
    path('trabajos/', views.trabajos, name="Trabajos"),
]

