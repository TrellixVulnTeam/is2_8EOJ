from django.db import models
from django.contrib.auth.models import AbstractUser
from proyectos.models import Proyecto

class User(AbstractUser):
    """ Usuario que tiene admitido realizar loggeo en el sistema """
    cedula = models.CharField(max_length=10)


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'



# Equipos para evitar agregar individualmente los usuarios al proyecto
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True, blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
            return f"El equipo {self.nombre} esta asignado al proyecto {self.proyecto}"