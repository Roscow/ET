
from django.conf.urls import include , url
from Apps.Mantencion.views import index, prueba,cosa,inicio, nueva_orden, problemas
from . import views



urlpatterns = [
    url(r'^prueba', prueba ),
    url(r'^$', index  ),
    url(r'^cosa', cosa ),
    url(r'^nueva_orden', views.nueva_orden, name='nueva_orden'),
    url(r'^problemas', views.problemas, name='problemas'),
    url(r'^conexion', views.opciones_conectar, name='conexion_opc'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^listado_tecnico', views.listado_tecnicos, name='listado_tecnicos'),
    url(r'^listado_ordenes', views.listado_ordenes, name='listado_ordenes'),
    url(r'^listado_asignaciones', views.listado_asignaciones, name='listado_asignaciones'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

]
