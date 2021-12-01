from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.controller.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
