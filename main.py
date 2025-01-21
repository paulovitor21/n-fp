# main
import logging
from scripts.process_data import processar_arquivo

# configuração de loggin
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def main():
    try:
        # caminho do arquivo
        xlsb_file = r"C:\Users\Paulo\Documents\Trabalho\n-fp\nf-p.xlsb"
        # processar arquivo
        processar_arquivo(xlsb_file)
    except Exception as e:
        logging.error(f"Ocorreu um erro na execução do processo: {e}")
        logging.exception("Detalhes do erro: ")
    
if __name__ == "__main__":
    main()