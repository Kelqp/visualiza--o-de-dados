import duckdb
conn = duckdb.connect(r"C:\Users\kelvin.pessoa\Documents\Kelvin Pessoal\visualização de dados\Banco de Dados\sihrd5.duckdb")
# Imprime todas as tabelas do banco de dados
print(conn.execute("SHOW TABLES").fetchdf()['column_name'].tolist())