import argparse

def get_parse() -> argparse.ArgumentParser:

    parse = argparse.ArgumentParser()
    
    # --- Items
    parse_item   = parse.add_argument_group("Items")
    parse_item.add_argument("-ui", "--update",          action="store_true", help="Begin to download missing files")
    parse_item.add_argument("-ni", "--new-item",        action="store_true", help="Create new item based on name link and folder")
    parse_item.add_argument("-di", "--del-item",        action="store_true", help="Delete specific item")
    parse_item.add_argument("-ei", "--edit-item",                            help="Edit items --name --folder and --link")
    parse_item.add_argument("-li", "--list-items",      action="store_true", help="List all items. If --group used will list all items in a group")
    
    # --- Values
    parse_values = parse.add_argument_group("Values")
    parse_values.add_argument("-n",  "--name",                               help="Specify name of item/setting")
    parse_values.add_argument("-f",  "--folder",                             help="Specify folder path of the item")
    parse_values.add_argument("-l",  "--link",                               help="Specify link of the item")
    parse_values.add_argument("-v",  "--value",                              help="Specify value of specific setting")
    parse_values.add_argument("-g",  "--group",                              help="Specify group name")

    # --- Config
    parse_config = parse.add_argument_group("Config")
    parse_config.add_argument("-lc", "--list-config",   action="store_true", help="List all available settings")
    parse_config.add_argument("-sc", "--set-config",    action="store_true", help="Change value of single setting")

    # --- Groups
    parse_groups = parse.add_argument_group("Groups")
    parse_groups.add_argument("-lg", "--list-groups",   action="store_true", help="List all created groups")
    parse_groups.add_argument("-pi", "--put-item",      action="store_true", help="Add an item --name into a --group")
    parse_groups.add_argument("-ti", "--take-item",     action="store_true", help="Remove an item --name from a --group")
    parse_groups.add_argument("-cg", "--clear-group",   action="store_true", help="Delete whole --group")

    # --- Other
    parse_other = parse.add_argument_group("Other")
    parse_other.add_argument("--here",                  action="store_true", help="Ignore the --folder variable and download in current path instead")
    parse_other.add_argument("--spread",                action="store_true", help="Create separate folders for each item if --here is used")

    return parse