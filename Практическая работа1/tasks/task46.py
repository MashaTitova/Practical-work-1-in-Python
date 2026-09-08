import json
def task46(data):
    with open("data.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Словарь сохранён в файл data.json")

    with open("data.json", "r") as f:
        loaded_data = json.load(f)

    print("Прочитанный словарь:", loaded_data)