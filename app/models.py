# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	nombre = models.CharField(max_length=80)
	slogan = models.CharField(max_length=150)

	def __unicode__(self):
		return self.nombre

class Articulo(models.Model):
	titulo = models.CharField(max_length=140)
	autor = models.ForeignKey(User)	
	contenido = models.TextField()
	imagen = models.URLField()
	slug = models.SlugField()
	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.titulo

class Etiqueta(models.Model):
	nombre = models.CharField(max_length=50)
	articulo = models.ManyToManyField(Articulo)

	def __unicode__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	slug = models.SlugField()
	padre = models.ForeignKey('Categoria',null=True)

	articulo = models.ManyToManyField(Articulo)	

	def __unicode__(self):
		return self.nombre

class Comentario(models.Model):
	titulo = models.CharField(max_length=80)

	articulo = models.ForeignKey(Articulo)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)

	#models.
	#	CASCADE
	#	PROTECT
	#	SET_NULL
	#	SET_DEFAULT / NOTA: Debe existir un valor default=__ 
	#	DO_NOTHING

	#usuario = models.OneToOneField(User)
	contenido = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.titulo