import os
import pandas as pd
import logging
from pyxlsb import open_workbook
import openpyxl

def convert_xlsb_to_xlsx(xlsb_file, output_dir="converted_files"):
    # Certifique-se de que o diretório de saída existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Nome do arquivo de saída
    xlsx_file = os.path.join(output_dir, os.path.splitext(os.path.basename(xlsb_file))[0] + ".xlsx")

    # Abre o arquivo XLSB e lê todas as abas
    with open_workbook(xlsb_file) as wb:
        wb_out = openpyxl.Workbook()  # Cria um novo arquivo XLSX
        first_sheet = True

        for sheetname in wb.sheets:
            with wb.get_sheet(sheetname) as sheet:
                if first_sheet:
                    ws = wb_out.active  # Para a primeira aba
                    ws.title = sheetname
                    first_sheet = False
                else:
                    ws = wb_out.create_sheet(title=sheetname)

                for row in sheet.rows():
                    ws.append([item.v for item in row])

        # Salva o arquivo XLSX
        wb_out.save(xlsx_file)

    return xlsx_file
