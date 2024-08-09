import os
import subprocess
import parsing as par
import classes as clas
import helper as hlp
import folders as folds
import options as opts

def main():
    folds.prep_folds()
    parse = par.get_args()

    # NEW PACK
    if parse.new:

        pack = clas.Pack(parse.new)
        if os.path.exists(pack.path):
            print("Pack already exists")
            return

        pack.save()
        print(f"Created new pack: {pack.name}")
        return
    
    # REMOVE PACK
    if parse.delete:

        path = os.path.join(clas.pack_path, parse.delete+".json")
        if not os.path.exists(path):
            print("Pack does not exist")
            return

        os.remove(path) 
        print(f"Removed pack: {pack.delete}")   

    # LIST PACKS
    if parse.list_packs:

        packs = os.listdir(clas.pack_path)
        
        vt = hlp.VisualTable(["Name", "Item count"], 3)

        if len(packs)>0:
            for p in packs:
                pack = clas.Pack(os.path.splitext(p)[0])
                vt.add_row([pack.name, len(pack.items)])
            print("\n"+str(vt))
            return

        else:
            print("No packs created yet")
            return

    # ADD ITEM
    if parse.add:

        pack = clas.Pack(parse.add)
        if not os.path.exists(pack.path):
            print(f"Pack '{pack.name}' does not exist")

        name = parse.name
        folder = parse.folder
        link = parse.link

        if not name:   print("--name Argument is required"); return
        if not folder: print("--folder Argument is required"); return
        if not link:   print("--link Argument is required"); return

        if pack.get_item(name):
            print(f"Item '{name}' already exists")
            return

        pack.add_item(name, folder, link)
        pack.save()

        print(
            f"\nAdded item to '{pack.name}' of properties:\n"+
            f" - Name   : {name}\n"+
            f" - Folder : {folder}\n"+
            f" - Link   : {link}\n"
        )
        return
    
    # REMOVE ITEM
    if parse.rem:

        pack = clas.Pack(parse.rem)
        if not os.path.exists(pack.path):
            print(f"Pack '{parse.rem}' does not exist")
            return
        
        if not parse.name:
            print(f"You need to specify item --name")
            return
        
        if not pack.get_item(parse.name):
            print(f"Item '{parse.name}' does not exist")
            return
        
        pack.rem_item(parse.name)
        pack.save()
        print(f"Deleted item '{parse.name}' from '{parse.rem}'")
        return

    # LIST ITEMS
    if parse.list_items:

        path = os.path.join(clas.pack_path, parse.list_items+".json")
        if not os.path.exists(path):
            print(f"Pack '{parse.list_items}' does not exist")
            return

        pack = clas.Pack(parse.list_items)
        vt = hlp.VisualTable(["Name", "Folder", "link"], 3)

        for i in pack.items:
            vt.add_row([i.name, i.folder, i.link])
        
        print(f"Items of pack '{pack.name}' looks like this:\n")
        print(vt)
        return
    
    # UPDATE DIR
    if parse.update:

        pack = clas.Pack(parse.update)
        if not os.path.exists(pack.path):
            print(f"Pack '{parse.update}' does not exist")
            return
        
        options = opts.OptDrawer()
        opt = options.get_opt("browser")

        for item in pack.items:
            command = f"gallery-dl --cookies-from-browser {opt.value} -D {item.folder} {item.link}"
            print(f"Running command: {command}")
            os.system(command)
    
    # EDIT ITEM
    if parse.edit:

        pack = clas.Pack(parse.edit)
        if not os.path.exists(pack.path):
            print(f"Pack '{parse.edit}' does not exist")
            return
        
        if not parse.name:
            print(f"You need to specify item --name")
            return
        
        item = pack.get_item(parse.name)
        if not item:
            print(f"Item '{parse.name}' does not exist")
            return
        
        vt = hlp.VisualTable(["Type", "Folder", "Link"], 3)
        vt.add_row(["Orignal", item.folder, item.link])

        name = parse.name
        folder = parse.folder
        link = parse.link

        if not folder: folder = None
        if not link:   link   = None

        vt.add_row(["New", folder, link])

        pack.edit_item(name, None, folder, link)
        pack.save()

        print(f"Edited properties of '{item.name}' from '{pack.name}':\n")
        print(vt)

    # LIST SETTINGS
    if parse.list_settings:

        vt = hlp.VisualTable(["Name", "Type", "Value", "Accepted Values"], 3)
        options = opts.OptDrawer()

        for opt in options.options:
            name = opt.name
            vtype = opt.value_type
            value = str(opt.value)
            if opt.allowed: allowed = ",".join([str(v) for v in opt.allowed])
            else: allowed = "Any"

            vt.add_row([name, vtype, value, allowed])
        
        print("User Settings:\n")
        print(vt)
        return

    # CHANGE SETTINGS
    if parse.setting:

        options = opts.OptDrawer()
        opt = options.get_opt(parse.setting)

        if not opt:
            print(f"Setting of name '{parse.setting}' does not exist")
            return
        
        if not parse.value:
            print(f"You must specify --value")
            return
        
        try:
            try: value = opts.type_map[opt.value_type](parse.value)
            except: raise opts.TypeNotAllowed

            opt.set_value(value)
            options.save()

            print(f"Successfully set '{opt.name}' value to '{opt.value}'")
            return
        
        except opts.ValueNotAllowed: print(f"Value '{parse.value}' is not accepted by '{opt.name}'")
        except opts.TypeNotAllowed:  print(f"Wrong type of --value")

    # LOCATION
    if parse.data_location: print(folds.get_data_location()); return
    if parse.open_data_location: subprocess.Popen(["explorer.exe", folds.get_data_location()], creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: print("Process stopped by the user")