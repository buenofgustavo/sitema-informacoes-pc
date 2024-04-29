from src.main.esconder_janela.esconder_janela import hide_console_window
from src.main.conexao_a_internet.verificar_conxão import is_connected
from src.main.obter_e_registrar.obter_e_registrar import obter_e_registrar_informacoes
from src.main.token.gerar_token import gerar_token
from src.main.fazer_solicitacao_http.solicitacao import fazer_solicitacao

import time

def main():

    hide_console_window()

    while True:
        time.sleep(0 * 30)
        if is_connected():
            dados = obter_e_registrar_informacoes()
            token = gerar_token(dados[2])
            response = fazer_solicitacao(token, dados)
            if response.status_code == 200:
                print("Solicitação bem-sucedida!")
            else:
                print("Falha na solicitação. Status code:", response.status_code)

        else:
            print("Sem conexão com a internet. Aguardando...")
        
        time.sleep(30 * 60)

        

if __name__ == "__main__":
    main()