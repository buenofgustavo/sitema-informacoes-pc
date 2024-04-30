import requests
import json

def fazer_solicitacao(token, dados):
    url = 'http://187.32.51.50:7892/computadores'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Origin': 'http://your_origin_here.com'
    }
    dados_json = criar_json_nomeado(dados)
    print(dados_json)
    response = requests.post(url, json=dados_json, headers=headers)
    return response

def criar_json_nomeado(dados):
    # Definindo os nomes dos campos
    nomes_campos = [
        "nomeUsuario",
        "nomeComputador",
        "enderecoMac",
        "localizacao",
        "memoriaRam",
        "capacidadeArmazenamento",
        "marca",
        "modelo",
        "processador",
        "sistemaOperacional",
        "makroInstalado",
        "versaoMakro"
        
    ]

    # Criando um dicionário com os nomes dos campos como chaves
    json_nomeado = {nome: valor for nome, valor in zip(nomes_campos, dados)}

    return json_nomeado