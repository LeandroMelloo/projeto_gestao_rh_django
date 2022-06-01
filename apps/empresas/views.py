from django.views.generic.edit import CreateView

from .models import EmpresaModel


class EmpresaView(CreateView):
    models = EmpresaModel
    fields = ['nome']
