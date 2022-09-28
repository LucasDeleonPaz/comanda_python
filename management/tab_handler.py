from utils.json_handler import read_json, read_table_json
from datetime import datetime

dia = str(datetime.today())
hora = (dia.split(" ")[1]).split(".")[0]
hoje = f"{datetime.now().strftime('%d')}/{datetime.now().strftime('%m')}/{datetime.now().strftime('%y')} {hora}"

def calculate_tab (name: str):

    path_name = 'menu.json'

    dataframe_menu = read_json(path_name)
    dataframe_consumo = read_table_json()

    table = dataframe_consumo[name]
    count = 0
    for item in dataframe_menu:
        for item_consumido in table:
            if item_consumido['id'] == item['id']:
                count += item['price'] * item_consumido['amount']
                
    result = {
        "subtotal": count,
        "created_at": hoje
    }

    return result


