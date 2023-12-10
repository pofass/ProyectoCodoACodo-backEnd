from django.db import models

# Create your models here.


class Empleado(models.Model):
    name = models.CharField(max_length=20, verbose_name = 'Nombre')
    nombreRubro = models.CharField(max_length=20, null=True)
    descripción = models.TextField()
    image = models.ImageField(verbose_name='imagen', upload_to='empleadosEnQuienesSomos')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de modificación')
    

    def __str__(self) -> str:
        return self.name

