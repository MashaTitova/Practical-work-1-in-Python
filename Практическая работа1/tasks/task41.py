from pathlib import *
def task41(file_path, new_string):
    path = Path(file_path)
    with path.open("a+") as f:
        if not new_string.endswith("\n"):
            new_string += "\n"
        f.write(new_string)

        f.seek(0)

        lines = f.readlines()
        print(f"Количество строк в файле: {len(lines)}")

        f.seek(0)
        file_text = f.read()
        print("Содержимое файла:")
        print(file_text)
