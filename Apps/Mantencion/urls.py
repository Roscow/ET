
from django.conf.urls import include , url
from Apps.Mantencion.views import index, prueba,cosa,inicio, nueva_orden
from . import views


urlpatterns = [
    url(r'^prueba', prueba ),
    url(r'^$', index  ),
    url(r'^cosa', cosa ),
    url(r'^nueva_orden', views.nueva_orden, name='nueva_orden'),
]
