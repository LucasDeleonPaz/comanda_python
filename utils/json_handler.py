from hashlib import new
import ujson as json

def read_json(path_name: str):
    try:
        with open(path_name, "r", encoding="utf8") as dataframe:
            return json.load(dataframe)
    except:
        return []

def write_json(path_name: str, data: dict):
    df = read_json(path_name)

    new_item = {
        "id": len(df)+1,
        **data
    }

    df.append(new_item)    
    with open(path_name, "w", encoding="utf8") as dataframe:
        json.dump(df, dataframe)


    return new_item

def read_table_json ():
    with open('tables.json', 'r', encoding="utf8") as dataframe:
        return json.load(dataframe)

def write_table_json (name: str, lista: dict):
    df = read_table_json()
    try:
        table = df[name]
        table.append(lista)
    except:
        df[name] = [lista]
    try:
        with open('tables.json', 'w', encoding="utf8") as dataframe:
            json.dump(df, dataframe)
        return df[name]
    except:
        return ""
