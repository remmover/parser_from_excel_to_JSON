import json
import os


def process_json_file(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    data["common:info:none"] = "None"

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


FOLDER_PATH = "locales"


for json_file in os.listdir(FOLDER_PATH):
    if json_file.endswith(".json") and "english" in json_file:
        full_path = os.path.join(FOLDER_PATH, json_file)
        process_json_file(full_path)
