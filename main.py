import pandas as pd
import json
import os


def excel_to_json(excel_file):
    KEY_COLUMN = 'id-key'
    VALUE_COLUMN = 'english'
    EXTRA_VALUE_COLUMN = 'other column'

    filename = os.path.splitext(excel_file)[0][2:]
    xls = pd.ExcelFile(excel_file)
    sheet_names = xls.sheet_names

    data = {}
    keys = []
    for sheet_name in sheet_names:

        df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[KEY_COLUMN, VALUE_COLUMN, EXTRA_VALUE_COLUMN])

        data[f"-------------- {sheet_name} --------------"] = f"-------------- {sheet_name} --------------"

        if df[VALUE_COLUMN].isnull().all():
            if EXTRA_VALUE_COLUMN and not df[EXTRA_VALUE_COLUMN].isnull().all():
                VALUE_COLUMN = EXTRA_VALUE_COLUMN
            else:
                print("Error: Both value column and extra value column are empty. Please enter different column names.")
                return

        for index, row in df.iterrows():
            key = row[KEY_COLUMN]
            value = row[VALUE_COLUMN]

            if (pd.notna(key) and key != ' ') and (pd.notna(value) and value != ' '):
                if key not in keys:
                    keys.append(key)

                    data[key] = value
                else:
                    raise Exception(f"Key with this name already exists: {key}")

    os.makedirs("locales", exist_ok=True)

    json_file = f"locales/{filename}.json"
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


FOLDER_PATH = "."
excel_files = [file for file in os.listdir(FOLDER_PATH) if file.endswith(".xlsx")]

for excel_file in excel_files:
    excel_to_json(os.path.join(FOLDER_PATH, excel_file))

# import pandas as pd
# import json
# import os
#
#
# def excel_to_json(excel_file):
#     KEY_COLUMN = 'id-key'
#     VALUE_COLUMN = 'other column'
#     EXTRA_VALUE_COLUMN = 'english'
#
#     filename = os.path.splitext(os.path.basename(excel_file))[0]
#     xls = pd.ExcelFile(excel_file)
#     sheet_names = xls.sheet_names
#
#     data = {}
#     keys = []
#     for sheet_name in sheet_names:
#
#         df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[KEY_COLUMN, VALUE_COLUMN, EXTRA_VALUE_COLUMN])
#
#         data[f"-------------- {sheet_name} --------------"] = f"-------------- {sheet_name} --------------"
#
#         if df[VALUE_COLUMN].isnull().all():
#             if EXTRA_VALUE_COLUMN and not df[EXTRA_VALUE_COLUMN].isnull().all():
#                 VALUE_COLUMN = EXTRA_VALUE_COLUMN
#             else:
#                 print("Error: Both value column and extra value column are empty. Please enter different column names.")
#                 return
#
#         for index, row in df.iterrows():
#             key = row[KEY_COLUMN]
#             value = row[VALUE_COLUMN]
#
#             if (pd.notna(key) and key != ' ') and (pd.notna(value) and value != ' '):
#                 if key not in keys:
#                     keys.append(key)
#
#                     data[key] = value
#                 else:
#                     raise Exception(f"Key with this name already exists: {key}")
#
#     os.makedirs("locales", exist_ok=True)
#
#     json_file = os.path.join("locales", f"{filename}.json")
#     with open(json_file, 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
#
#
# folder_path = "excel"
# excel_files = [file for file in os.listdir(folder_path) if file.endswith(".xlsx")]
#
# for excel_file in excel_files:
#     excel_to_json(os.path.join(folder_path, excel_file))
