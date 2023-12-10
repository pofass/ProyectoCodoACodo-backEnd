from django.contrib import admin
from .models import Empleado



# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields=("name",)

admin.site.register(Empleado, EmpleadoAdmin)