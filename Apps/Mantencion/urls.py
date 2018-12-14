
from django.conf.urls import include , url
from Apps.Mantencion.views import nueva_orden,nuevo_cliente
from . import views



urlpatterns = [
    url(r'^nueva_orden/(?P<id>[0-9]+)/$', views.nueva_orden, name='nueva_orden'),
 #   url(r'^conexion', views.opciones_conectar, name='conexion_opc'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^listado_tecnico', views.listado_tecnicos, name='listado_tecnicos'),
	url(r'^nuevo_cliente', views.nuevo_cliente, name='nuevo_cliente'),
    url(r'^listado_ordenes', views.listado_ordenes, name='listado_ordenes'),
	url(r'^todas_ordenes', views.todas_ordenes, name='todas_ordenes'),
    url(r'^listado_asignaciones', views.listado_asignaciones, name='listado_asignaciones'),

]
