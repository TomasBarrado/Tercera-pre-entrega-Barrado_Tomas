from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar_dueño/', views.registrar_dueño, name='registrar_dueño'),
    path('registrar_paciente/', views.registrar_paciente, name='registrar_paciente'),
    path('registrar_veterinario/', views.registrar_veterinario, name='registrar_veterinario'),
    path('buscar/', views.buscar, name='buscar'),
    
]