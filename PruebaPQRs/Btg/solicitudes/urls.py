from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('gestionPeticiones/', views.gestion_peticiones),
    path('crearPeticion/', views.crear_peticion),
    path('registrarPeticion/', views.registrar_peticion),
    path('eliminarPeticion/<num_radicado>', views.eliminar_peticion),
    path('agradoUsuarioP/<num_radicado>', views.agrado_usuarioP),
    path('hacerReclamoP/<num_radicado>', views.hacer_reclamo_p),
    path('registrarReclamoP/', views.registrar_reclamo_p),
    path('verPeticion/<num_radicado>', views.ver_peticion),
    path('gestionQuejas/', views.gestion_quejas), 
    path('crearQueja/', views.crear_queja),
    path('registrarQueja/', views.registrar_queja),
    path('eliminarQueja/<num_radicado>', views.eliminar_queja),
    path('agradoUsuarioQ/<num_radicado>', views.agrado_usuarioQ),
    path('hacerReclamoQ/<num_radicado>', views.hacer_reclamo_q),
    path('registrarReclamoQ/', views.registrar_reclamo_q),
    path('verQueja/<num_radicado>', views.ver_queja),
]
