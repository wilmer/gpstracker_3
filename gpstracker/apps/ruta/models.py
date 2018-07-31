from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=70)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	domicilio = models.TextField()


	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellidos)


class Ruta(models.Model):
	persona = models.ForeignKey(Persona, null=True, blank=True)
	latitud = models.CharField(max_length=200)
	longitud = models.CharField(max_length=200)
	fecha_creacion=models.DateField()
	altitud=models.CharField(max_length=200)
	velocidad=models.CharField(max_length=200)
	direccion_brujula=models.CharField(max_length=200)
	precision=models.CharField(max_length=200)
	proveedor=models.CharField(max_length=200)

