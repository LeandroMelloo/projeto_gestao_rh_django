from django.db import models


class EmpresaModel(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome da empresa")

    def __int__(self):
        return self.id
    
    def __str__(self):
        return self.nome

