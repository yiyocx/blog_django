from django.db import models

class Articulo(models.Model):
	titulo = models.CharField(max_length=80)
	contenido = models.TextField()
	url_img = models.ImageField(upload_to="articulo")
	fecha = models.DateTimeField(auto_now_add=True)
