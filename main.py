import json
import os

import pandas as pd


def excel_to_json(excel_file):
    KEY_COLUMN = "Keys for developers"
    VALUE_COLUMN = "extra-value-translate"
    EXTRA_VALUE_COLUMN = "value-translate"

    filename = os.path.splitext(excel_file)[0][2:]
    xls = pd.ExcelFile(excel_file)
    sheet_names = xls.sheet_names

    data = {}
    keys = []
    for sheet_name in sheet_names:
        df = pd.read_excel(
            excel_file,
            sheet_name=sheet_name,
            usecols=[KEY_COLUMN, VALUE_COLUMN, EXTRA_VALUE_COLUMN],
        )

        data[
            f"-------------- {sheet_name} --------------"
        ] = f"-------------- {sheet_name} --------------"

        for index, row in df.iterrows():
            key = row[KEY_COLUMN]

            if pd.notna(key) and key != " ":
                if key not in keys:
                    keys.append(key)

                    value = row[VALUE_COLUMN]
                    extra_value = row[EXTRA_VALUE_COLUMN]

                    if pd.notna(value) and value != " ":
                        data[key] = value
                    elif pd.notna(extra_value) and extra_value != " ":
                        print(key, extra_value)
                        data[key] = extra_value

                else:
                    raise Exception(f"Key with this name already exists: {key}")

    os.makedirs("locales", exist_ok=True)

    json_file = f"locales/{filename}.json"
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


FOLDER_PATH = "."
excel_files = [file for file in os.listdir(FOLDER_PATH) if file.endswith(".xlsx")]

for excel_file in excel_files:
    excel_to_json(os.path.join(FOLDER_PATH, excel_file))
