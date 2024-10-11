import argparse

def get_parse() -> argparse.ArgumentParser:

    parse = argparse.ArgumentParser()
    
    parse.add_argument("-ni", "--new-item", action="store_true", help="Create new item based on name link and folder")
    parse.add_argument("-di", "--del-item", action="store_true", help="Delete specific item, required --name argument")
    parse.add_argument("-e",  "--edit-item",                     help="Edit items --name --folder and --link")
    
    parse.add_argument("-n",  "--name",   help="Specify name of the item")
    parse.add_argument("-f",  "--folder", help="Specify folder path of the item")
    parse.add_argument("-l",  "--link",   help="Specify link of the item")

    parse.add_argument("-u",  "--update",     action="store_true", help="Begin to download missing files")
    parse.add_argument("-li", "--list-items", action="store_true", help="List all items")

    return parse