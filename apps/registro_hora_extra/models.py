from django.db import models
from apps.funcionarios.models import FuncionarioModel


class RegistroHoraExtraModel(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(FuncionarioModel, on_delete=models.PROTECT) # PROTECT -> primeiro deletar o Registro Hora Extra, depois deletar funcionario

    def __int__(self):
        return self.id

    def __str__(self):
        return self.motivo
