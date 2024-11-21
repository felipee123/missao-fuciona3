from datetime import timedelta

from produtos.settings import SECRET_KEY

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # Tempo de vida do token de acesso
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),    # Tempo de vida do token de atualização
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,  # Chave de assinatura
    'AUTH_HEADER_TYPES': ('Bearer',),
}
