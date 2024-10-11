# Libraries
import os
import rich
import rich.table

# Stagings
import pars
import color
import json
import fold
import stage

# CONTROL
parse = pars.get_parse().parse_args()
fold.prepare()

# --- Update
if parse.update:

    # Get name
    name = parse.name
    if not name: name = input(" Item Name > ")
    if not name: print(color.red("You must specify item name")); quit()

    # Get
    data = fold.get_items()
    item = stage.find_item(name, data)
    if not item: print(color.red(f"Item '{name}' does not exist")); quit()

    # Update
    cmd = stage.get_item_cmd(item)
    print(f"Running : {color.blue(cmd)}")
    os.system(cmd)
    print(color.green("Done!"))
    quit()

# --- New Item
if parse.new_item:
    
    # Get Variables
    if parse.name:   name   = parse.name
    else:            name   = input(" Name   > ")
    if parse.folder: folder = parse.folder
    else:            folder = input(" Folder > ")
    if parse.link:   link   = parse.link
    else:            link   = input(" Link   > ")

    # Fill Missing
    error_block = False
    if not name:   print(color.red("Name cannot be empty"));   error_block = True
    if not folder: print(color.red("Folder cannot be empty")); error_block = True
    if not link:   print(color.red("Link cannot be empty"));   error_block = True
    elif not link.startswith("https://"): print(color.red("Link must be URL")); error_block = True
    if error_block: quit()

    # Prepare data dict
    data = fold.get_items()
    if stage.find_item(name, data):
        print(f"Item '{name}' already exists"); quit()
    
    # Add to list and save
    data.append({
        "name"   : name,
        "folder" : folder,
        "link"   : link
    })

    fold.set_items(data)
    print(color.green("Item has been created successfully"))
    quit()

# --- List Items
if parse.list_items:

    # Get Items
    json_path = fold.get_path("items.json")
    if os.path.exists(json_path): data :list[dict] = json.load(open(json_path, "r"))
    else:                         data :list[dict] = []

    # If not items
    if len(data) == 0:
        print(color.red("List is empty")); quit()

    # Display
    table = rich.table.Table()
    table.add_column("Name",   style="green")
    table.add_column("Folder", style="yellow")
    table.add_column("Name",   style="cyan")

    for i in data:
        table.add_row(i["name"], i["folder"], i["link"])
    
    rich.print(table)
    quit()

# --- Delete Item
if parse.del_item:

    name = parse.name
    if not name: name = input(" Item Name > ")
    if not name: print(color.red("You must specify item name")); quit()
    
    # Get
    data = fold.get_items()
    item = stage.find_item(name, data)
    if not item: print(color.red(f"Item '{name}' does not exist")); quit()

    # Final
    if not stage.are_you_sure():
        print(color.red("Deletion cancelled")); quit()

    data.remove(item)
    fold.set_items(data)
    print(color.green("Items has been deleted"))

    quit()

# --- Edit Item
if parse.edit_item:

    # Get
    name = parse.edit_item
    data = fold.get_items()
    item = stage.find_item(name, data)
    if not item: print(color.red("Item does not exist")); quit()

    # Prep
    new_name   = parse.name
    new_folder = parse.folder
    new_link   = parse.link

    # Manual input
    if (not new_name and not new_folder and not new_link):
        print("Specify new values. Leave blank if you want the value to remain the same")
        new_name   = input(" Name   > ")
        new_folder = input(" Folder > ")
        new_link   = input(" Link   > ")

        # If still empty
        if (not new_name and not new_folder and not new_link):
            print(color.red("Nothing changed")); quit()
    
    # Change values
    if new_name:   item["name"]   = new_name
    if new_folder: item["folder"] = new_folder
    if new_link:   item["link"]   = new_link

    # Final
    fold.set_items(data)
    print(color.green("Item has been edited"))
    quit()