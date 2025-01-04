from datetime import datetime
import os

def extrair_data(file_path):
    data_modificacao = os.path.getmtime(file_path)
    data_arquivo = datetime.fromtimestamp(data_modificacao).strftime('%Y-%m-%d')
    return data_arquivo