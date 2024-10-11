import os
import platform
import json

def get_appdata():
    system = platform.system()

    match system:
        case "Windows": return os.getenv("APPDATA") # Windows
        case "Darwin":  return os.path.expanduser("~/Library/Application Support/") # MacOS
        case _:         return os.path.expanduser("~/.local/share/") # Linux

ROOT_PATH    = os.path.normpath(os.path.join(get_appdata(), "Gilg"))

def prepare():
    if not os.path.exists(ROOT_PATH):
        os.mkdir(ROOT_PATH)

def get_path(sub_path:str) -> str:
    return os.path.normpath(os.path.join(ROOT_PATH, sub_path))

def get_items() -> list[dict]:
    json_path = get_path("items.json")
    if os.path.exists(json_path):
        return json.load(open(json_path, "r"))
    return []

def set_items(data:list[dict]) -> None:
    json_path = get_path("items.json")
    json.dump(data, open(json_path, "w"))