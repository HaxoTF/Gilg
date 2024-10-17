import json
import os
import fold
import stage

def get_list() -> list[str]:
    list_path = fold.get_path("groups")
    return [os.path.splitext(g)[0] for g in os.listdir(list_path) if g.endswith(".json")]

def group_exists(name:str) -> bool:
    return os.path.exists(fold.get_path(f"groups/{name}.json"))

def get_group(name:str) -> list[str]:
    path = fold.get_path(f"groups/{name}.json")
    if not os.path.exists(path): return None

    with open(path, "r") as f:
        group :list[str] = json.load(f)
    
    group.sort()
    return group

def set_group(name:str, group:list[str]):
    group = clean_group(group)
    path = fold.get_path(f"groups/{name}.json")
    with open(path, "w") as f:
        json.dump(group, f, indent=4)

def rem_group(name:str):
    path = fold.get_path(f"groups/{name}.json")
    if os.path.exists(path):
        os.remove(path)

def get_group_items(grp:list[str]) -> list[dict]:
    result :list[dict] = []
    data = fold.get_items()

    for item in data:
        if item["name"] in grp:
            result.append(item)
    
    result.sort(key=lambda x: x["name"])
    return result

def clean_group(grp:list[str]) -> list[dict]:
    return [i["name"] for i in get_group_items(grp)] 