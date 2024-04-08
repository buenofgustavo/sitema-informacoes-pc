import pyodbc
    
def enviar_dados_unique(conn, dados):
    endereco_mac = dados[2]  # Índice 2 representa o EnderecoMAC nos seus dados
    
    try:
        cursor = conn.cursor()
        
        # Verificar se o EnderecoMAC já existe na tabela uniqueComputadores
        cursor.execute("SELECT COUNT(*) FROM unique_computadores WHERE endereco_mac = ?", (endereco_mac,))
        row = cursor.fetchone()
        if row[0] > 0:
            
            # Se o EnderecoMAC existir na tabela, atualizar os dados
            cursor.execute("""
                UPDATE unique_computadores
                SET nome_usuario = ?, nome_computador = ?, localizacao = ?, memoria_ram = ?, capacidade_armazenamento = ?, marca = ?, modelo = ?, processador = ?, sistema_operacional = ?, makro_instalado = ?, versao_makro = ?
                WHERE endereco_mac = ?
            """, (*dados[:2], *dados[3:], endereco_mac))  # Ignorando o EnderecoMAC no final dos dados
        else:
            # Se o EnderecoMAC não existir na tabela, inserir os dados
            cursor.execute("""
            INSERT INTO unique_computadores (nome_usuario, nome_computador, endereco_mac, localizacao, memoria_ram, capacidade_armazenamento, marca, modelo, processador, sistema_operacional, makro_instalado, versao_makro)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, dados)
        
        conn.commit()
        print("Dados enviados para o banco de dados com sucesso!")
    except pyodbc.Error as e:
        print(f"Erro ao enviar dados para o banco de dados: {str(e)}")