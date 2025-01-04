import pandas as pd

def load_excel(file_path: str, sheet_name) -> pd.DataFrame:
    """Carregar arquivo excel para retornar um Dataframe

    Args:
        file_path (str): [description]

    Returns:
        pd.DataFrame: [description]
    """
    xls = pd.ExcelFile(file_path)
    df_pph = xls.parse(sheet_name, header=0)
    return df_pph