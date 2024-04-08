import psutil

def verificar_processo_makro():
    
    nome_processo = "MakroService.exe"

    for processo in psutil.process_iter():
        try:
            # Verifica se o nome do processo corresponde ao fornecido
            if processo.name().lower() == nome_processo.lower():
                return "INSTALADO"
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return "NÃO INSTALADO"

def obter_versao_do_makro():
    
    caminho_arquivo = r"C:\Program Files (x86)\Makrosystems\Makrolock\bugreports.txt"  # Correção no nome do arquivo

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:  # Especificando a codificação como 'utf-8'
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.strip().startswith("version"):
                    versao = linha.split(":")[1].strip()
                    return versao
        return "Versão não encontrada"
    except Exception as e:
        return f"Erro ao obter versão"
    

    makro = verificar_processo_makro()

    versao_makro = obter_versao_do_makro()
