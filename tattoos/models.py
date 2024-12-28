from django.db import models

class Tattoos(models.Model):
    name = models.CharField(max_lenght= 30, default = "No definido")
    description = models.CharField(max_lenght= 255, default = "Sin descripcion definida")
    price = models.DecimalField(max_digits = 2, default = 1.00)
    photo = models.ImageField(upload_to=None)
    author = models.CharField(max_lenght= 30, default = "Xavier")