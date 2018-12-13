from django.shortcuts import render, redirect
from  django.http import HttpResponse
from .forms import nuevaOrdenForm
from .models import Orden, Tecnico
from django.contrib.auth import logout



# Create your views here.


def prueba(request):
    return HttpResponse("probando")


def index(request):
     return render(request, 'templates/index.html' )


def cosa(request):
    return HttpResponse("cosa")


def inicio(request):
    return render(request, 'templates/base.html' )

def problemas(request):
    return render(request, 'templates/problema_conexion.html' )

def opciones_conectar(request):
    return render(request, 'templates/conexion_opc.html' )


def nueva_orden(request):
     if request.method =="POST":
        form = nuevaOrdenForm(request.POST)
        if form.is_valid():
            Orden = form.save(commit=True)
            Orden.save()
            return redirect('/admin/')
     else:
        form = nuevaOrdenForm()
     return render(request, 'templates/nueva_orden.html', {'form': form})


def listado_tecnicos(request):
    tecnicos_list = Tecnico.objects.all()  
    contexto = {'tecnicos':tecnicos_list}
    return render(request, 'templates/listado_tecnicos.html', contexto)
    

def listado_ordenes(request):
    ordenes_list = Orden.objects.all()  
    contexto = {'ordenes':ordenes_list}
    return render(request, 'templates/listado_ordenes.html', contexto)
    
