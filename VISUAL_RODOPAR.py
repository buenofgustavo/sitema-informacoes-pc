from src.main.esconder_janela.esconder_janela import hide_console_window
from src.main.conexao_a_internet.verificar_conxão import is_connected
from src.main.banco_de_dados.conectar_ao_banco import conectar_banco_dados
from src.main.obter_e_registrar.obter_e_registrar import obter_e_registrar_informacoes
import time

def main():

    hide_console_window()

    while True:
        time.sleep(0 * 60)
        if is_connected():
            conn = conectar_banco_dados()
            if conn:
                obter_e_registrar_informacoes(conn)
                conn.close()
        else:
            print("Sem conexão com a internet. Aguardando...")
        time.sleep(30 * 60)

if __name__ == "__main__":
    main()