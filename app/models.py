from django.db import models

class Articulo(models.Model):
	titulo = models.CharField(max_length=80)
	contenido = models.TextField()
	url_img = models.ImageField(upload_to="articulo")
	fecha = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.titulo

	def reciente(self):
		import datetime as d, time as t
		a = t.localtime()

		if self.fecha < d.date(a.tm_year, a.tm_mon, a.tm_mday-2):
			return False
		else:
			return True