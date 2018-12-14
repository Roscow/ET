from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from . import views 
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView

#from django.urls import path 


urlpatterns = [
	url(r'^$', views.index,name='index'),
	url(r'^admin/login/', LoginView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^', include ('Apps.Mantencion.urls')),
 	url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
	url(r'^s/',include('social.apps.django_app.urls',namespace='social2')),
	url(r'^oauth/', include('social_django.urls', namespace='social')),
	url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),
]
