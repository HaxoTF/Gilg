import json
import os
import fold
import vhold

def get_config() -> list[dict]:
    json_path = fold.get_path("config.json")

    config :list[dict] = []
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            config = json.load(f)

    return fill_missing(config)

def set_config(config:list[dict]):
    json_path = fold.get_path("config.json")
    with open(json_path, "w") as f:
        json.dump(config, f)

def find_value(name:str, config:list[dict]) -> dict:
    for v in config:
        if v["name"] == name:
            return v

def fill_missing(config:list[dict]) -> list[dict]:
    config = config[:]
    for v in vhold.DEFAULT_CONFIG:
        if not find_value(v["name"], config):
            config.append({
                "name"  : v["name"],
                "value" : v["value"]
            })
            
    config.sort(key=lambda x: x["name"])
    return config

def value_allowed(name:str, value:str) -> bool:
    default :dict = find_value(name, vhold.DEFAULT_CONFIG)
    if "allowed" not in default: return True
    if value in default["allowed"]: return True
    return False