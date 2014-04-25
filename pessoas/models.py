from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length='100', blank=False, null=False)
<<<<<<< HEAD
    
=======

>>>>>>> ed271e821956b564a159ec5d478d3e7c31ad071e
    email = models.CharField(max_length='100', blank=True, null=True)

    telefone = models.CharField(max_length='20', blank=True, null=True)

    logradouro = models.CharField(max_length='200', blank=True, null=True)