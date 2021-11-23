from django.db import models
 
# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    
class Peticion(models.Model):
    id_usuario = models.IntegerField()
    num_radicado = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateField()
    respuesta_admin = models.BooleanField()
    desc_respuesta = models.CharField(max_length=200)
    fecha_respuesta = models.DateField()
    usuario_agrado = models.BooleanField()
    hay_reclamo = models.BooleanField()
    reclamo = models.IntegerField()
    
class Queja(models.Model):
    id_usuario = models.IntegerField()
    num_radicado = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateField()
    respuesta_admin = models.BooleanField()
    desc_respuesta = models.CharField(max_length=200)
    fecha_respuesta = models.DateField()
    usuario_agrado = models.BooleanField()
    hay_reclamo = models.BooleanField()
    reclamo = models.IntegerField()
    
class ReclamoP(models.Model):
    num_peticion = models.IntegerField()
    num_radicado = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateField()
    
class ReclamoQ(models.Model):
    num_queja = models.IntegerField()
    num_radicado = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateField()