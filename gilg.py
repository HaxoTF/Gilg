# Libraries
import os
import rich
import rich.table
import sys

# Stagings
import color
import config
import fold
import groups
import pars
import stage
import vhold

# CONTROL
parse = pars.get_parse().parse_args()
fold.prepare()

# --- Update
if parse.update:

    # Single item
    if parse.name:
        name = parse.name

        # Get
        data = fold.get_items()
        item = stage.find_item(name, data)
        if not item: color.fast_error(f"Item '{name}' does not exist")
        stage.set_terminal_title(f"Updating {name}...")

        # Update
        if parse.here:
            root = fold.gen_free_path("gilg")
            if parse.spread: folder = os.path.join(root, item["name"])
            else:            folder = root
            cmd = stage.get_item_cmd(item, folder)
        else:
            cmd = stage.get_item_cmd(item)
        
        print(f"\n\nRunning : {color.blue(cmd)}\n")
        os.system(cmd)
    
    # Whole group
    elif parse.group:
        name  = parse.group
        grp   = groups.get_group(name)
        items = groups.get_group_items(grp)

        total   = len(grp)
        current = 0 

        if parse.here: root = fold.gen_free_path("gilg")
        for i in items:

            current += 1
            percent  = int(current/total*100)
            stage.set_terminal_title(f"{percent}% - {i['name']}")

            if parse.here:
                if parse.spread: folder = os.path.join(root, i["name"])
                else:            folder = root
                cmd = stage.get_item_cmd(i, folder)
            else:
                cmd = stage.get_item_cmd(i)

            print(f"\n\nItem    : {color.green(i['name'])}")
            print(    f"Running : {color.blue(cmd)}\n")
            os.system(cmd)
    
    # None
    else: color.fast_error("You must specify item --name or --group")
        
    print(color.green("Done!"))
    sys.exit()



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
    if error_block: sys.exit()

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
    sys.exit()

# --- List Items
if parse.list_items:

    # Data
    data = fold.get_items()
    if len(data) == 0:
        color.fast_error("Item list is empty"); sys.exit()

    # Display
    if parse.group:
        grp = groups.get_group(parse.group)
        if not grp: color.fast_error(f"Group '{parse.group}' does not exist")

        table = rich.table.Table(title=f"Group '{parse.group}' Items")
        table.add_column("Name",   style="green")
        table.add_column("Folder", style="yellow")
        table.add_column("Link",   style="cyan")

        for item in groups.get_group_items(grp):
            table.add_row(item["name"], item["folder"], item["link"])

    else:
        table = rich.table.Table(title="Items")
        table.add_column("Name",   style="green")
        table.add_column("Folder", style="yellow")
        table.add_column("Link",   style="cyan")

        for i in data:
            table.add_row(i["name"], i["folder"], i["link"])
    
    rich.print(table)
    sys.exit()

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

    sys.exit()

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
    sys.exit()



# ----- [ C O N F I G ] -----

# --- List Config
if parse.list_config:

    # Get config
    con = config.get_config()

    # Table collumns
    table = rich.table.Table(title="Config")
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
    sys.exit()

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
    sys.exit()



# ----- [ G R O U P S ] -----

# --- List Groups
if parse.list_groups:

    gps = groups.get_list()
    if len(gps)==0: color.fast_error("Group list is empty")

    table = rich.table.Table(title="Groups")
    table.add_column("Name",  style="blue")
    table.add_column("Items", style="yellow")
    
    lines :list[str] = []
    for g_name in gps:
        grp = groups.get_group(g_name)
        item_count = len(grp)

        table.add_row(g_name, str(item_count))
    
    rich.print(table)


# --- Put Item
if parse.put_item:
    
    # Group name
    g_name = parse.group
    if not g_name: g_name = input(" Group Name > ")
    if not g_name: color.fast_error("You must specify --group.")
    grp = groups.get_group(g_name)
    if not grp: grp = []
    
    # Item name
    i_name = parse.name
    if not i_name: i_name = input(" Item Name  > ")
    if not i_name: color.fast_error("You must specify --name")

    # Get data
    data = fold.get_items()
    item = stage.find_item(i_name, data)
    if not item: color.fast_error(f"Item '{i_name}' does not exist")
    if i_name in grp: color.fast_error(f"Item '{i_name}' is already in group '{g_name}'")

    # Finally
    grp.append(i_name)
    groups.set_group(g_name, grp)
    print(color.green(f"Item '{i_name}' has been added to group '{g_name}'"))
    sys.exit()


# --- Take Item
if parse.take_item:
    
    # Group name
    g_name = parse.group
    if not g_name: g_name = input(" Group Name > ")
    if not g_name: color.fast_error("You must specify --group.")
    grp = groups.get_group(g_name)
    if not grp: grp = []
    
    # Item name
    i_name = parse.name
    if not i_name: i_name = input(" Item Name  > ")
    if not i_name: color.fast_error("You must specify --name")

    # Get data
    data = fold.get_items()
    item = stage.find_item(i_name, data)
    if not item: color.fast_error(f"Item '{i_name}' does not exist")
    if i_name not in grp: color.fast_error(f"Item '{i_name}' is not in group '{g_name}'")

    # Finally
    grp.remove(i_name)
    if len(grp)>0: groups.set_group(g_name, grp)
    else:          groups.rem_group(g_name)
    print(color.green(f"Item '{i_name}' has been taken from group '{g_name}'"))
    sys.exit()

# --- Clear Group
if parse.clear_group:

    g_name = parse.group
    if not g_name: g_name = input(" Group Name > ")
    if not g_name: color.fast_error("You must specify --group.")

    if not groups.get_group(g_name): color.fast_error(f"Group '{g_name}' does not exist")
    if not stage.are_you_sure():     color.fast_error("Deletion cancelled")

    groups.rem_group(g_name)
    print(color.green(f"Group '{g_name}' has been deleted"))
    sys.exit()