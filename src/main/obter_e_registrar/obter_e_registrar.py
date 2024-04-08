import os
import socket
from getmac import get_mac_address as gma
import geocoder
import psutil
import wmi
import platform


from src.main.banco_de_dados.enviar_dados import enviar_dados_para_banco_dados
from src.main.banco_de_dados.enviar_tabela_unique import enviar_dados_unique
from src.main.makro.verificar_makro import verificar_processo_makro
from src.main.makro.verificar_makro import obter_versao_do_makro


def obter_e_registrar_informacoes(conn):
    user = os.getlogin()
    nome_do_computador = socket.gethostname()
    MAC = gma()


    location = geocoder.ip('me')

    total_memory = psutil.virtual_memory().total
    total_memory_gb = total_memory / (1024 ** 3)
    total_memory = "{:.2f}".format(total_memory_gb)

    particao_atual = psutil.disk_partitions()[0].mountpoint
    try:
        info_particao_atual = psutil.disk_usage(particao_atual)
        capacidade_particao_atual_gb = info_particao_atual.total / (1024 ** 3)
        capacidade = f'{capacidade_particao_atual_gb:.2f}'

    except Exception as e:
        capacidade = "Erro ao obter informações sobre a partição"

    if location:
        city = location.city
    else:
        city = "Localização não encontrada"

    c = wmi.WMI()
    for system in c.Win32_ComputerSystem():
        marca = system.Manufacturer

    
    c = wmi.WMI()
    for system in c.Win32_ComputerSystem():
        modelo = system.Model

    c = wmi.WMI()
    for cpu in c.Win32_Processor():
        processador = cpu.Name

    sistema_operacional = f"{platform.system()} {platform.release()}"

    makro = verificar_processo_makro()

    versao_makro = obter_versao_do_makro()

    print(user)
    print(nome_do_computador)
    print(MAC)
    print(city)
    print(total_memory)
    print(capacidade)
    print(marca)
    print(modelo)
    print(processador)
    print(sistema_operacional)
    print(makro)
    print(versao_makro)

    dados = [user, nome_do_computador, MAC, city, total_memory, capacidade, marca, modelo, processador, sistema_operacional, makro, versao_makro]

    enviar_dados_para_banco_dados(conn, dados)
    enviar_dados_unique(conn, dados)