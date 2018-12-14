from django.contrib import admin
from Apps.Mantencion.models import Cliente, Orden, Asignacion


admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(Asignacion)

