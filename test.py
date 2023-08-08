import json
import os
from collections import defaultdict

import pandas as pd


def excel_to_json(excel_file):
    KEY_COLUMN = "Keys for developers"
    VALUE_COLUMN = "extra-value-translate"
    EXTRA_VALUE_COLUMN = "value-translate"

    filename = os.path.splitext(excel_file)[0][5:]
    xls = pd.ExcelFile(excel_file)
    sheet_names = xls.sheet_names

    data = defaultdict(str)
    for sheet_name in sheet_names:
        df = pd.read_excel(
            excel_file,
            sheet_name=sheet_name,
            usecols=[KEY_COLUMN, VALUE_COLUMN, EXTRA_VALUE_COLUMN],
        )
        data[
            f"-------------- {sheet_name} --------------"
        ] = f"-------------- {sheet_name} --------------"

        for _, row in df.iterrows():
            key = row[KEY_COLUMN].strip()
            if key:
                if key in data:
                    raise Exception(f"Key with this name already exists: {key}")

                value = row[VALUE_COLUMN].strip()
                extra_value = row[EXTRA_VALUE_COLUMN].strip()

                if value:
                    data[key.replace(" ", "")] = value
                elif extra_value:
                    data[key.replace(" ", "")] = value

    os.makedirs("locales", exist_ok=True)

    json_file = os.path.join("locales", f"{filename}.json")
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


FOLDER_PATH = "."
excel_files = [file for file in os.listdir(FOLDER_PATH) if file.endswith(".xlsx")]

for excel_file in excel_files:
    excel_to_json(os.path.join(FOLDER_PATH, excel_file))
