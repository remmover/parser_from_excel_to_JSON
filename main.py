import pandas as pd
import json
import os


def excel_to_json(excel_file):
    filename = os.path.splitext(excel_file)[0][5:]
    xls = pd.ExcelFile(excel_file)
    sheet_names = xls.sheet_names

    data = {}
    keys = []
    for sheet_name in sheet_names:

        df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=["Keys for developers", filename])

        data[f"-------------- {sheet_name} --------------"] = f"-------------- {sheet_name} --------------"

        for index, row in df.iterrows():
            key = row["Keys for developers"]
            value = row[filename]

            if (pd.notna(key) and key != ' ') and (pd.notna(value) and value != ' '):
                if key not in keys:
                    keys.append(key)
                    data[key.replace(' ', '')] = value
                else:
                    raise Exception(f"Key with this name already exists: {key}")

    os.makedirs("locales", exist_ok=True)

    json_file = f"locales/{filename}.json"
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


folder_path = "."
excel_files = [file for file in os.listdir(folder_path) if file.endswith(".xlsx")]

for excel_file in excel_files:
    excel_to_json(os.path.join(folder_path, excel_file))
