from django.db import models
from apps.funcionarios.models import FuncionarioModel


class DocumentoModel(models.Model):
    descricao = models.CharField(max_length=100)
    funcionario = models.ForeignKey(FuncionarioModel, on_delete=models.PROTECT)

    def __int__(self):
        return self.id

    def __str__(self):
        return self.descricao
