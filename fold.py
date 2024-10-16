import os
import platform
import json
import vhold

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

    for folder in vhold.BASE_FOLDERS:
        full_path = get_path(folder)
        if not os.path.exists(full_path):
            os.mkdir(full_path)

def get_path(sub_path:str) -> str:
    return os.path.normpath(os.path.join(ROOT_PATH, sub_path))

def get_items() -> list[dict]:
    json_path = get_path("items.json")
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            return json.load(f)
    return []

def set_items(data:list[dict]) -> None:
    json_path = get_path("items.json")
    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)

def gen_free_path(prename="untitled", ext="", root=None):
    if not root: root = os.getcwd()
    full_path = os.path.join(root, f"{prename}{ext}")

    i = 0
    while os.path.exists(full_path):
        full_path = os.path.join(root, f"{prename} {i}{ext}")
        i += 1
    
    return full_path