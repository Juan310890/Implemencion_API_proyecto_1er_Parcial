from django.contrib import admin
from deportistas.models import Deportista, Sede, Competencia, Representante

# Register your models here.
admin.site.register(Deportista)
admin.site.register(Sede)
admin.site.register(Competencia)
admin.site.register(Representante)
