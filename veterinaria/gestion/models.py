from django.db import models

class Dueño(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
