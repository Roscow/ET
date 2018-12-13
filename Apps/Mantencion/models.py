
from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    nombre = models.CharField(primary_key=True,max_length=50)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.CharField(max_length=16)
    correo= models.EmailField(max_length=60)

    def __str__(self):
        return self.nombre

class Tecnico(models.Model):
    correo = models.EmailField(max_length=60)
    contraseña = models.CharField(null=False, max_length=20)
    nombre = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.nombre

class Ascensor(models.Model):
    id_ascensor = models.CharField(primary_key=True, max_length=50)
    modelo = models.CharField(null=False, max_length=20)
    
    def __str__(self):
        return self.id_ascensor




class Asignacion(models.Model):
    asignacion_id = models.CharField(primary_key=True, max_length=50) 
    cliente = models.ForeignKey(Cliente , on_delete=models.CASCADE)
    tecnico = models.ManyToManyField(Tecnico)
    Estado =  models.CharField(max_length=50)

    def __str__(self):
        return self.asignacion_id


class Orden(models.Model):
    id_ascensor = models.ForeignKey(Ascensor, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente , on_delete=models.CASCADE)
    tecnico = models.ManyToManyField(Tecnico)
    folio = models.OneToOneField(Asignacion, primary_key=True, on_delete=models.CASCADE)
    fecha = models.DateField(blank=True, null=False)
    hora_inicio = models.CharField(max_length=50)
    hora_termino =  models.CharField(max_length=50)
    num_fallas = models.IntegerField()
    num_reparaciones = models.IntegerField()
    num_repuestos = models.IntegerField()

    def __str__(self):
        return self.folio