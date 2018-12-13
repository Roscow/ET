from django.contrib import admin
from Apps.Mantencion.models import Cliente, Tecnico, Orden, Ascensor, Asignacion


admin.site.register(Cliente)
admin.site.register(Tecnico)
admin.site.register(Orden)
admin.site.register(Ascensor)
admin.site.register(Asignacion)

