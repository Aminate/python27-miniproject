import json
def write_to_json(data:dict):
    with open('db.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

def get_db():
    try:
        with open("db.json") as file:
            return json.load(file) #мы загружаем чтото с файла
    except:      #если файл не сущ или он пустой
        return {}
    
def get_pages():
    db = get_db()
    return list(db.keys())

    
    