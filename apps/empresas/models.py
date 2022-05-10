from django.db import models


class EmpresaModel(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome da empresa")

    class Meta:
        managed = True
        db_table = 'projeto_rh"."empresa'
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __int__(self):
        return self.id
    
    def __str__(self):
        return self.nome

