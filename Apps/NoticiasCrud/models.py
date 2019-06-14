from django.db import models

# Create your models here.

class NoticiasModelo(models.Model):
    titulo=models.CharField(max_length=100)
    resumen=models.CharField(max_length=500)
    detalle=models.CharField(max_length=10000)
    fecha=models.CharField(max_length=8)
    FAMILIAS=(('N', 'Noticia'), ('E', 'Evento'))
    Familia=models.CharField(max_length=1, choices=FAMILIAS, default='N')
