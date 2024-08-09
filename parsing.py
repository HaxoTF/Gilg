import argparse

def get_args():

    parse = argparse.ArgumentParser()

    # Pack Related
    pack_parse = parse.add_argument_group("Packs")
    pack_parse.add_argument("-U", "--update", type=str, help="Use pack data to update folder by downloading missing/new images/videos from LINK", metavar="PACK NAME")
    pack_parse.add_argument("--new",          type=str, help="Create new pack",   metavar="PACK NAME")
    pack_parse.add_argument("--delete",       type=str, help="Remove pack",       metavar="PACK NAME")

    # Item related
    item_parse = parse.add_argument_group("Items")
    item_parse.add_argument("--add",  type=str, help="Add an item to pack",      metavar="PACK NAME")
    item_parse.add_argument("--rem",  type=str, help="Remove an item from pack", metavar="PACK NAME")
    item_parse.add_argument("--edit", type=str, help="Change --folder or/and --link value of an item. Requires --name", metavar="PACK NAME")

    # Holders
    holder_parse = parse.add_argument_group("Holders")
    holder_parse.add_argument("-n", "--name",   type=str, help="Specify NAME argument of an item",   metavar="ITEM NAME")
    holder_parse.add_argument("-f", "--folder", type=str, help="Specify FOLDER argument of an item", metavar="PATH")
    holder_parse.add_argument("-l", "--link",   type=str, help="Specify LINK argument of an item",   metavar="URL")

    # Settings Related
    sett_parse = parse.add_argument_group("Settings")
    sett_parse.add_argument("-s", "--setting", type=str, help="Specify setting name to change it's --value", metavar="NAME")
    sett_parse.add_argument("-v", "--value",   type=str, help="Specify value name of a setting",           metavar="NAME")

    # Other Tools
    other_parse = parse.add_argument_group("Other Tools")
    other_parse.add_argument("-lp", "--list-packs",    action="store_true", help="List all packs in 'packs' folder")
    other_parse.add_argument("-li", "--list-items",    type=str,            help="List all items in pack",            metavar="PACK NAME")
    other_parse.add_argument("-ls", "--list-settings", action="store_true", help="List all settings and it's values")
    other_parse.add_argument("-dl", "--data-location", action="store_true", help="Displays location where Gilg data is stored")
    other_parse.add_argument("-odl", "--open-data-location", action="store_true", help="Opens location where Gilg data is stored in explorer.exe. Windows only")

    return parse.parse_args()