# Libraries
import os
import rich
import rich.table
import json

# Stagings
import color
import config
import fold
import pars
import stage
import vhold

# CONTROL
parse = pars.get_parse().parse_args()
fold.prepare()

# --- Update
if parse.update:

    # Get name
    name = parse.name
    if not name: name = input(" Item Name > ")
    if not name: color.fast_error("You must specify item name")

    # Get
    data = fold.get_items()
    item = stage.find_item(name, data)
    if not item: color.fast_error(f"Item '{name}' does not exist")

    # Update
    cmd = stage.get_item_cmd(item)
    print(f"Running : {color.blue(cmd)}")
    os.system(cmd)
    print(color.green("Done!"))
    quit()



# ----- [ I T E M S ] -----

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
    if not name:   color.fast_error("Name cannot be empty");   error_block = True
    if not folder: color.fast_error("Folder cannot be empty"); error_block = True
    if not link:   color.fast_error("Link cannot be empty");   error_block = True
    elif not link.startswith("https://"): color.fast_error("Link must be URL"); error_block = True
    if error_block: quit()

    # Prepare data dict
    data = fold.get_items()
    if stage.find_item(name, data):
        color.fast_error(f"Item '{name}' already exists")
    
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

    # Data
    data = fold.get_items()
    if len(data) == 0:
        color.fast_error("List is empty"); quit()

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
    if not name: color.fast_error("You must specify item name")
    
    # Get
    data = fold.get_items()
    item = stage.find_item(name, data)
    if not item: color.fast_error(f"Item '{name}' does not exist")

    # Final
    if not stage.are_you_sure():
        color.fast_error("Deletion cancelled")

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
    if not item: color.fast_error("Item does not exist")

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
            color.fast_error("Nothing changed")
    
    # Change values
    if new_name:   item["name"]   = new_name
    if new_folder: item["folder"] = new_folder
    if new_link:   item["link"]   = new_link

    # Final
    fold.set_items(data)
    print(color.green("Item has been edited"))
    quit()



# ----- [ C O N F I G ] -----

# --- List Config
if parse.list_config:

    # Get config
    con = config.get_config()

    # Table collumns
    table = rich.table.Table()
    table.add_column("Name",  style="blue")
    table.add_column("Value", style="green")

    # Table rows
    for c in con:
        allowed = config.find_value(c["name"], vhold.DEFAULT_CONFIG).get("allowed", None)
        if allowed:

            values = []
            for av in allowed:
                if av == c["value"]: values.append(av)
                else:                values.append(f"[red]{av}[/red]")
            
            table.add_row(c["name"], " ".join(values))
        
        else:
            table.add_row(c["name"], c["value"])

    # Display
    rich.print(table)
    quit()

# --- Set value
if parse.set_config:

    # Get config
    name = parse.name
    if not name: name = input(" Name  > ")
    if not name: color.fast_error("You must specify setting name")

    # Get config
    con = config.get_config()
    setting = config.find_value(name, con)
    if not setting: color.fast_error("Setting doesn't exist")

    # Value
    value = parse.value
    if not value: value = input(" Value > ")
    if not value: color.fast_error("You must specify new value")
    if not config.value_allowed(name, value):
        color.fast_error(f"Value '{value}' is not accepted by setting '{name}'")

    # Modify
    setting["value"] = value
    config.set_config(con)
    print(color.green(f"Setting '{name}' has been changed to '{value}'"))
    quit()