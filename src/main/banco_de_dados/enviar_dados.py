import pyodbc

def enviar_dados_para_banco_dados(conn, dados):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO computadores (nome_usuario, nome_computador, endereco_mac, localizacao, memoria_ram, capacidade_armazenamento, marca, modelo, processador, sistema_operacional, makro_instalado, versao_makro)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, dados)
        conn.commit()
        print("Dados enviados para o banco de dados com sucesso!")
    except pyodbc.Error as e:
        print(f"Erro ao enviar dados para o banco de dados: {str(e)}")

