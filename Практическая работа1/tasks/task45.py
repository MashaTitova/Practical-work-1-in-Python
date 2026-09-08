import pickle
def task45(lst):
    with open("data.pkl", "wb") as f:
        pickle.dump(lst, f)

    print("Список сохранён в файл data.pkl")

    with open("data.pkl", "rb") as f:
        loaded_data = pickle.load(f)

    print(loaded_data)
