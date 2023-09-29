import json

def get_json_data() -> None:
    json_file = open("users_data/data.json")
    data = json.load(json_file)
    return data
