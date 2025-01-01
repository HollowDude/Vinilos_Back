from django.db import models

class Tattoo(models.Model):
    name = models.CharField(max_length= 30, default = "No definido")
    description = models.CharField(max_length= 255, default = "Sin descripcion definida")
    price = models.DecimalField(max_digits = 5, decimal_places = 2, default = 1.00)
    photo = models.ImageField(blank='', default='', upload_to='photos/')
    author = models.CharField(max_length= 30, default = "Xavier")
    

    class Meta:
        verbose_name = "Tattoo"
        verbose_name_plural = "Tattoos"