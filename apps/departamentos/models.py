from django.db import models


class DepartamentoModel(models.Model):
    nome = models.CharField(max_length=70)

    def __int__(self):
        return self.id

    def __str__(self):
        return self.nome
