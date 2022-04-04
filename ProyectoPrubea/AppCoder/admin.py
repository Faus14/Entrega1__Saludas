from django.contrib import admin

from .models import persona,producto,horario

# Register your models here.
admin.site.register(persona)
admin.site.register(producto)
admin.site.register(horario)