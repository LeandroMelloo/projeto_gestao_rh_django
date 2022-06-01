from django.urls import path

from .views import EmpresaView

urlpatterns = [
    path('cadastrar', EmpresaView.as_view(), name='cadastrar_empresa'),
]
