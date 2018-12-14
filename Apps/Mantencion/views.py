from django.shortcuts import render, redirect,get_object_or_404
from  django.http import HttpResponse
from .forms import nuevaOrdenForm,nuevoClienteForm
from .models import Orden, Asignacion, Cliente
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test


@login_required
def nueva_orden(request,id):
    if request.method =="POST":
         form = nuevaOrdenForm(request.POST)
         if form.is_valid():
             Orden = form.save(commit=False)
             Orden.tecnico = request.user
             Orden.cliente = get_object_or_404(Cliente,id=id)
             Orden.save()
             return redirect('listado_ordenes')
    else:
        form = nuevaOrdenForm()
    asignaciones_list = Asignacion.objects.filter(tecnico = request.user)
    cliente = get_object_or_404(Cliente,id=id)
    return render(request, 'templates/nueva_orden.html', {'form': form,'asignaciones':asignaciones_list,'cliente':cliente})
	

@login_required
def listado_tecnicos(request):
    tecnicos_list = User.objects.filter(is_staff=True, is_superuser=False)
    return render(request, 'templates/listado_tecnicos.html', {'tecnicos': tecnicos_list})
  
@login_required
def listado_ordenes(request):
    ordenes_list = Orden.objects.filter(tecnico = request.user)  
    return render(request, 'templates/listado_ordenes.html', {'ordenes':ordenes_list})
    

#hacer filtro por tecnico
@login_required
def listado_asignaciones(request):
     asignaciones_list = Asignacion.objects.filter(tecnico = request.user)
     clientes_list = Cliente.objects.all()
     return render(request, 'templates/listado_asignaciones.html', {'asignaciones':asignaciones_list,'clientes':clientes_list})

@user_passes_test(lambda u: u.is_superuser)
def nuevo_cliente(request):
    if request.method =="POST":
        form = nuevoClienteForm(request.POST)
        if form.is_valid():
            x = form.save(commit=True)
            x.save()
            return redirect('/')
    else:
        form = nuevoClienteForm()
    return render(request, 'templates/nuevo_cliente.html', {'form': form})
	 
@user_passes_test(lambda u: u.is_superuser)
def todas_ordenes(request):
    ordenes_list = Orden.objects.all()
    return render(request, 'templates/todas_ordenes.html', {'ordenes':ordenes_list})
    