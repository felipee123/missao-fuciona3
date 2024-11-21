from django.urls import path # type: ignore
from mercado import views # type: ignore
from mercado.views import ExemploView, ProdutoListCreateView, ProdutoRetrieveUpdateDeleteView # type: ignore
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,  # Para obter tokens de acesso e atualização
    TokenRefreshView,     # Para atualizar o token de acesso
    TokenVerifyView       # Para verificar a validade do token
)

urlpatterns = [
    path('produto/novo/', views.produto_new, name='produto_new'),
    path('produto/sucesso/', views.produto_success, name='produto_success'),
    path('api/produtos/', ProdutoListCreateView.as_view(), name='produto-list-create'),
    path('api/produtos/<int:pk>/', ProdutoRetrieveUpdateDeleteView.as_view(), name='produto-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/protegida/', ExemploView.as_view(), name='rota_protegida'),
    
]