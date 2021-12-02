from django.views.generic.edit import CreateView
from apps.empresas.models import EmpresaModel


class EmpresaView(CreateView):
    models = EmpresaModel
    fields = ['nome']
