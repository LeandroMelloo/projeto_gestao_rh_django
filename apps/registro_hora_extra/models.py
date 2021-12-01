from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)

    def __int__(self):
        return self.id

    def __str__(self):
        return self.motivo
