
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from agenda import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('fornecedores.urls')),
    path('', include('clientes.urls')),
    path('', include('funcionarios.urls')),
    path('', include('produtos.urls')),
    path('', include('servicos.urls')),
    path('', include('agendamentos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)