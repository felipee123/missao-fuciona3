from django.urls import path # type: ignore
from mercado import views # type: ignore


urlpatterns = [
    path('produto/novo/', views.produto_new, name='produto_new'),
    path('produto/sucesso/', views.produto_success, name='produto_success'),
    # Defina outras URLs se necessário
]