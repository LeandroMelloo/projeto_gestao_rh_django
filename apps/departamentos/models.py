from django.db import models


class DepartamentoModel(models.Model):
    nome = models.CharField(max_length=70)

    class Meta:
        managed = True
        db_table = 'projeto_rh"."departamentos'
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __int__(self):
        return self.id

    def __str__(self):
        return self.nome
