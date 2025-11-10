from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_clinicanutricional, name='inicio_clinicanutricional'),

    # --- NUTRIÓLOGOS ---
    path('agregar_nutriologo/', views.agregar_nutriologo, name='agregar_nutriologo'),
    path('ver_nutriologos/', views.ver_nutriologos, name='ver_nutriologos'),
    path('actualizar_nutriologo/<int:id>/', views.actualizar_nutriologo, name='actualizar_nutriologo'),
    path('realizar_actualizacion_nutriologo/<int:id>/', views.realizar_actualizacion_nutriologo, name='realizar_actualizacion_nutriologo'),
    path('borrar_nutriologo/<int:id>/', views.borrar_nutriologo, name='borrar_nutriologo'),

    # --- PACIENTES ---
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('ver_pacientes/', views.ver_pacientes, name='ver_pacientes'),
    path('actualizar_paciente/<int:id>/', views.actualizar_paciente, name='actualizar_paciente'),
    path('realizar_actualizacion_paciente/<int:id>/', views.realizar_actualizacion_paciente, name='realizar_actualizacion_paciente'),
    path('borrar_paciente/<int:id>/', views.borrar_paciente, name='borrar_paciente'),

    # --- CITAS ---
    path('agregar_cita/', views.agregar_cita, name='agregar_cita'),
    path('ver_citas/', views.ver_citas, name='ver_citas'),
    path('actualizar_cita/<int:id>/', views.actualizar_cita, name='actualizar_cita'),
    path('realizar_actualizacion_cita/<int:id>/', views.realizar_actualizacion_cita, name='realizar_actualizacion_cita'),
    path('borrar_cita/<int:id>/', views.borrar_cita, name='borrar_cita'),
]
