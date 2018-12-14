from django import forms
from .models import Orden, Cliente
from django.forms import ModelForm, DateInput, DateField
import datetime

class nuevaOrdenForm(forms.ModelForm):
	
	class Meta:
		model = Orden
		fields = [
            'tecnico',
            'cliente' ,
            'fecha',
            'hora_inicio', 
            'hora_termino', 
            'ascensor_id',
            'ascensor_modelo',
            'fallas',
            'reparaciones',
            'repuestos', 
			]

		widgets = {

            'fecha':forms.SelectDateWidget(years=range(datetime.datetime.now().year - 100, datetime.datetime.now().year)),

			}

class nuevoClienteForm(forms.ModelForm):
	
	class Meta:
		model = Cliente
		fields = [
            'nombre',
            'direccion' ,
            'ciudad',
            'comuna', 
            'telefono', 
            'correo',

			]