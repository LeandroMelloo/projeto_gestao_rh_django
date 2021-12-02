from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import DepartamentoModel
from apps.empresas.models import EmpresaModel


class FuncionarioModel(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT) # PROTECT -> primeiro deletar o funcionario, depois deletar usuario
    departamento = models.ManyToManyField(DepartamentoModel) # ManyToManyField -> 1 Usuario <-> N Departamentos, um usuario irá possuir uma lista de departamentos
    empresa = models.ForeignKey(EmpresaModel, on_delete=models.PROTECT, null=True, blank=True) # PROTECT -> primeiro deletar o funcionario, depois deletar empresa

    def __int__(self):
        return self.id

    def __str__(self):
        return self.nome
