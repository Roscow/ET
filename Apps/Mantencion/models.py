
from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo= models.EmailField(max_length=60)

    def __str__(self):
        return self.nombre

'''
class Ascensor(models.Model):
    id_ascensor = models.CharField(primary_key=True, max_length=50)
    modelo = models.CharField(null=False, max_length=20)
    
    def __str__(self):
        return self.id_ascensor
'''


class Asignacion(models.Model):
    tecnico = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente , on_delete=models.CASCADE)
	
    class Meta:
        verbose_name_plural='Asignaciones'
        verbose_name='Asignación'

    def __str__(self):
        return "Tecnico: " + self.tecnico.username + " / " + "Cliente: " + self.cliente.__str__()


class Orden(models.Model):
    tecnico = models.ForeignKey('auth.User', on_delete=models.PROTECT,blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT,blank=True)
	
    fecha = models.DateField(blank=True, null=False)
    hora_inicio = models.TimeField(null=False)
    hora_termino =  models.TimeField(null=False)
    ascensor_id = models.CharField(max_length=50)
    ascensor_modelo = models.CharField(max_length=50,null=False)
    fallas = models.TextField(max_length=100)
    reparaciones = models.TextField(max_length=100)
    repuestos = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural='Órdenes'
        verbose_name='Orden'

    def __str__(self):
        return self.fecha.__str__() + " " + self.id.__str__()
