from django.db import models

class Piercing(models.Model):
    name = models.CharField(max_length= 30, default = "No definido")
    description = models.CharField(max_length= 255, default = "Sin descripcion definida")
    price = models.DecimalField(max_digits = 5, decimal_places = 2, default = 1.00)
    photo = models.ImageField(blank='', default='', upload_to='photos/')

    class Meta:
        verbose_name = "Piercing"
        verbose_name_plural = "Piercings"
    
