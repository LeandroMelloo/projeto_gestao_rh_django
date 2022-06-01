from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.funcionarios.models import FuncionarioModel


@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'controller/index.html', data)
