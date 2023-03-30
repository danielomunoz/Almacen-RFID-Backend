from django.db import models

import uuid

# Create your models here.


class Persona(models.Model):
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
	nombre = models.CharField(max_length=100, blank=False, null=False)
	email = models.CharField(max_length=50, blank=False, null=False)
	movil = models.CharField(max_length=15, blank=False, null=False)
	dni = models.CharField(max_length=15, blank=False, null=False)
	codigo_rfid = models.CharField(max_length=40, blank=False, null=False)
	imagen = models.CharField(max_length=100, blank=False, null=False)
	fecha_registro = models.IntegerField(blank=False, null=False)
	rol = models.CharField(max_length=20, blank=False, null=False)
	usuario = models.CharField(max_length=50, blank=False, null=False)
	password = models.CharField(max_length=50, blank=False, null=False)
	estado = models.CharField(max_length=20, blank=False, null=False)
	fecha_baja = models.IntegerField(blank=True, null=True)
	token_sesion = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.nombre

class Objeto(models.Model):
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
	nombre = models.CharField(max_length=100, blank=False, null=False)
	descripcion = models.CharField(max_length=200, blank=False, null=False)
	familia = models.CharField(max_length=50, blank=False, null=False)
	categoria = models.CharField(max_length=50, blank=False, null=False)
	subcategoria = models.CharField(max_length=50, blank=True, null=False)
	numero_serie = models.CharField(max_length=30, blank=False, null=False)
	estado_en_almacen = models.CharField(max_length=20, blank=False, null=False)
	fecha_alta = models.IntegerField(blank=False, null=False)
	responsable = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='responsable')
	propietario = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='propietario')
	localizacion = models.CharField(max_length=100, blank=False, null=False)
	fecha_ultima_accion = models.IntegerField(blank=False, null=False)
	codigo_rfid = models.CharField(max_length=40, blank=False, null=False)
	imagen = models.CharField(max_length=100, blank=False, null=False)
	estado_objeto = models.CharField(max_length=20, blank=False, null=False)
	fecha_baja = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.nombre


class Accion(models.Model):
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
	tipo = models.CharField(max_length=15, blank=False, null=False)
	persona = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='persona')
	objeto = models.ForeignKey(Objeto, on_delete=models.PROTECT, related_name='objeto')
	fecha = models.IntegerField(blank=False, null=False)

	def __str__(self):
		return self.id
