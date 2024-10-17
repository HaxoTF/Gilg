import os
import json
import fold

# dirs structure: [ { name:"", path:"" } ]

def get_roots() -> list[dict]:
    json_path = fold.get_path("dirs.json")
    if not os.path.exists(json_path): return []
    
    with open(json_path, "r") as f:
        dirs = json.load(f)
    return dirs

def set_roots(dirs:list[dict]):
    json_path = fold.get_path("dirs.json")
    with open(json_path, "w") as f:
        json.dump(dirs, f)

def find_root(name:str, dirs:list[dict]) -> dict:
    for d in dirs:
        if d["name"] == name:
            return d
        
def find_path(name:str, dirs:list[dict]) -> dict:
    for d in dirs:
        if f"#{d['name']}" == name:
            return d["path"]