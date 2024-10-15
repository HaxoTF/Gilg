import config

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

def get_item_cmd(item:dict):
    browser = config.quick_value("browser")
    return f'gallery-dl --cookies-from-browser {browser} -D "{item["folder"]}" {item["link"]}'