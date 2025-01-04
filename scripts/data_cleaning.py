from datetime import datetime
import pandas as pd

def clean_data(df_nfp: pd.DataFrame):
    # Identifique as colunas que provavelmente são datas
    date_columns = [col for col in df_nfp.columns if isinstance(col, (int, float))]

    # Converta os nomes das colunas para datas
    new_column_names = {
    col: pd.to_datetime(col, unit='D', origin='1899-12-30').strftime('%Y-%m-%d')
    for col in date_columns
    }

    # Renomear as colunas no DataFrame
    df_nfp.rename(columns=new_column_names, inplace=True)

    # remover colunas nao usadas
    df_nfp = df_nfp.drop(columns=['Target ID', 'Line', 'Update', 'Demand ID', 'Model', 'Suffix', 'Tool', 'BOM Date', 'Original Due Date', 'MERC PO NO', 'MERC PO Qty', 'MERC Supplier Name', 'Mix Member', 'Mix Group', 'Mix Rate', 'OQC Pass', 'Sys.Cancel', 'RNUM', 'Demand Type', 'Source Type', 'Map Qty', 'RSD', 'Due Date', 'PST', 'Ship To Name', 'Bucket', 'Urgent Back Order','Mapping Order', 'Ship Method', 'Mapping Qty', 'Mapping Date','PST-Due Date', 'GSBS Doc. Due Date', 'Booking ID', 'Vessel Name', 'Ship Alloc. Initial POL ETD', 'Lot Qty',   'Remain Qty', 'Comment1', 'Comment2', 'CBM', 'Market', 'Product Type', 'PL2 Code', 'PL4 Code', 'Chassis', 'Country', 'Expire Date', 'ATP Date','Back Order', 'Final Dest.', 'Closed Qty', 'Parent Closed Qty', 'Result Qty', 'Period Qty', 'Hold Date', 'SMS', 'Item Status','UIT', 'Set Pno', 'UPH', 'Ori. Demand ID', 'Splitted Demand ID', 'Ship To Code', 'W/O', 'W/O Line',       'W/O PST', 'W/O PET', 'W/O Complete', 'Bill To Name', 'Long-term Prod(M6)', 'BOM', 'New', 'Priority', 'PET', 'W/O Status', 'Latest T/T'])

    # Derretimento das colunas
    id_vars = ["Plant", "Model.Suffix"]  # Colunas que permanecerão fixas
    value_vars = [col for col in df_nfp.columns if col not in id_vars]  # Colunas que serão derretidas

    # Derreter as colunas de data
    df_nfp = pd.melt(
        df_nfp,
        id_vars=id_vars,
        value_vars=value_vars,
        var_name="date",    # Nome da coluna que armazenará as datas
        value_name="quantity"  # Nome da coluna que armazenará os valores
    )

    # Converter a coluna "date" para o tipo datetime, se necessário
    df_nfp["date"] = pd.to_datetime(df_nfp["date"])

    # Substituir valores null na coluna 'quantity' por 0
    df_nfp["quantity"] = df_nfp["quantity"].fillna(0).astype(int)

    

    return df_nfp


   


   
