from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20, verbose_name = 'título')
    price = models.DecimalField(decimal_places=2, max_digits=10000, verbose_name = 'precio')
    description = models.TextField(blank=True, null=True, verbose_name = 'descripción')
    image = models.ImageField(verbose_name = 'imagen', upload_to="products")
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'fecha de modificación')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['-created']
        