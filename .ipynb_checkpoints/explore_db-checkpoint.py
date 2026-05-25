import duckdb
import pandas as pd

# Conecta ao banco de dados DuckDB
conn = duckdb.connect(r"C:\Users\kelvin.pessoa\Documents\Kelvin Pessoal\visualização de dados\Banco de Dados\sihrd5.duckdb")

print("=" * 100)
print("EXPLORAÇÃO DAS TABELAS E COLUNAS DO DUCKDB")
print("=" * 100)

# 1. Obter lista de todas as tabelas
tables_df = conn.execute("SHOW TABLES").fetchdf()

if tables_df.empty:
    print("O banco de dados está vazio ou não possui tabelas criadas.")
else:
    tabelas = tables_df['name'].tolist()
    print(f"Foram encontradas {len(tabelas)} tabela(s) no banco:\n")
    
    # 2. Iterar sobre cada tabela e mapear suas colunas
    for tabela in tabelas:
        print(f"--- Tabela: '{tabela}' ---")
        try:
            # Puxamos as informações (describe da tabela)
            cols_df = conn.execute(f"DESCRIBE {tabela}").fetchdf()
            
            # Mostramos o nome e tipo de dado da coluna
            for index, row in cols_df.iterrows():
                print(f"  - {row['column_name']} ({row['column_type']})")
                
            print("\n")
        except Exception as e:
            print(f"  Erro ao detalhar a tabela {tabela}: {e}\n")

# Encerra as conexões com segurança
conn.close()