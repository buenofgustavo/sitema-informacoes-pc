
import jwt
import datetime
from datetime import timedelta, timezone

def gerar_token(endereco_mac):
    nome_usuario = 'System@123tdm'
    secret_key = 'System@123'
    agora_utc = datetime.datetime.now(timezone.utc)
    tempo_expiracao = agora_utc + timedelta(minutes=10)
    payload = {
        'nomeUsuario': nome_usuario,
        'enderecoMac': endereco_mac,
        'iss': 'sistema-computadores',
        'exp': tempo_expiracao  # Tempo de expiração do token
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token