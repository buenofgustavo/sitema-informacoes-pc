import pyodbc

def enviar_dados_para_banco_dados(conn, dados):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO computadores (NomeUsuario, NomeComputador, EnderecoMAC, Localizacao, MemoriaRAM, CapacidadeArmazenamento, marca, modelo, processador, sistemaOperacional, makroInstalado, versaoMakro)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, dados)
        conn.commit()
        print("Dados enviados para o banco de dados com sucesso!")
    except pyodbc.Error as e:
        print(f"Erro ao enviar dados para o banco de dados: {str(e)}")