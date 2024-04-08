import pyodbc

def conectar_banco_dados():
    try:
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=192.168.0.17,1433;'
            'DATABASE=dbcentraltiweb;'
            'UID=sa;'
            'PWD=System@123;'
        )
        return conn
    except pyodbc.Error as e:
        print(f"Erro ao conectar ao banco de dados: {str(e)}")
        return None