from django.urls import path
from .views import EmpresaView

urlpatterns = [
    path('novo', EmpresaView.as_view(), name='create_empresa'),
]