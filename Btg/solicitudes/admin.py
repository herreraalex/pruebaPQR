from django.contrib import admin
from .models import Usuario, Peticion, Queja, ReclamoP, ReclamoQ

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Peticion)
admin.site.register(Queja)
admin.site.register(ReclamoP)
admin.site.register(ReclamoQ)
