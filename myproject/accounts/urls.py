from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Agrega más rutas según sea necesario para tu aplicación
]
