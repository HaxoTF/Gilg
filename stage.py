import config
import os
import sys

def are_you_sure(msg:str=None) -> bool:
    if msg: text = msg + " (y/n) "
    else:   text = "Are you sure? (y/n): "

    reply = input(text)
    if reply.lower() in ["yes", "y"]: return True
    return False

def find_item(name:str, data:list[dict]) -> dict:
    for item in data:
        if item["name"] == name:
            return item

def get_item_cmd(item:dict, folder=None):
    browser = config.quick_value("browser")
    if not folder: folder = item["folder"]
    return f'gallery-dl --cookies-from-browser {browser} -D "{folder}" {item["link"]}'

def set_terminal_title(title):
    if os.name == "nt": # Windows
        os.system(f"title {title}")

    elif os.name == "unix": # Linux, MacOS
        sys.stdout.write(f'\33]0;{title}\a')
        sys.stdout.flush()