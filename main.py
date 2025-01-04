import os
from scripts.db_connection import SessionLocal, engine
from scripts.models import Base
from scripts.data_loader import load_excel
from scripts.data_cleaning import clean_data
from scripts.db_operations import save_to_db
from scripts.extract_data_file import extrair_data
import pandas as pd
from datetime import datetime

def main():
    # Cria as tabelas no banco de dados
    Base.metadata.create_all(bind=engine)

    # Criar sessão
    db = SessionLocal()
    
    try:
        # Carregar os dados
        file_path = r"arquivo_convertido.xlsx"
        sheet_name = 'Sheet1'
        df_nfp = load_excel(file_path, sheet_name)

        # Extrair data do arquivo
        file_date = extrair_data(file_path)
        print(f"Data do ARQUIVO -> {file_date}")

    
        # Limpar os dados
        df_nfp = clean_data(df_nfp)

        # Salvar no banco
        save_to_db(df_nfp, db, file_date)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()