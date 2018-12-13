from django import forms
from .models import Orden
from django.forms import ModelForm, DateInput, DateField
import datetime

class nuevaOrdenForm(forms.ModelForm):
	
	class Meta:
		model = Orden
		fields = [
            'folio',
            'id_ascensor' ,
            'cliente',
            'tecnico', 
            'fecha', 
            'hora_inicio',
            'hora_termino',
            'num_fallas',
            'num_reparaciones',
            'num_repuestos', 
			]

		widgets = {
            'folio':forms.TextInput(),
            'id_ascensor':forms.Select(),
            'cliente':forms.Select(),
            'tecnico':forms.CheckboxSelectMultiple(),
            'fecha':forms.SelectDateWidget(years=range(datetime.datetime.now().year - 100, datetime.datetime.now().year)),
            'hora_inicio':forms.TextInput(),
            'hora_termino':forms.TextInput(),
            'num_fallas':forms.TextInput(),
            'num_reparaciones':forms.TextInput(),
            'num_repuestos':forms.TextInput(),      
			}
