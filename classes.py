import os
import json
import shutil
from typing import Dict
import folders as folds

pack_path = folds.get_fold("Gilg/packs")

class Item:
    def __init__(self, name:str, folder:str, link:str):

        self.name = name
        self.folder = folder
        self.link = link
        

class Pack:
    def __init__(self, name:str):

        self.name  :str        = name
        self.items :list[Item] = []
        self.path  :str        = os.path.join(pack_path, name+".json")
        if os.path.exists(self.path): self.load() 
    
    # SAVE
    def save(self) -> None:
        
        data = []
        for i in self.items:
            data.append({
                "name"   : i.name,
                "folder" : i.folder,
                "link"   : i.link
            })

        with open(self.path, "w") as f:
            json.dump(data, f, indent=3)
    
    # LOAD
    def load(self) -> None:

        with open(self.path, "r") as f:
            data :list[Dict] = json.load(f)
        
        for i in data:
            self.items.append(Item( i["name"], i["folder"], i["link"] ))
    
    
    # ADD ITEM
    def add_item(self, name:str, folder:str, link:str) -> None:
        self.items.append(Item(name, folder, link))

    # GET ITEM
    def get_item(self, name:str) -> Item:
        for i in self.items:
            if i.name == name: return i
    
    # REMOVE ITEM
    def rem_item(self, name:str) -> None:
        item = self.get_item(name)
        if item: self.items.remove(item)
    
    # EDIT ITEM
    def edit_item(self, name:str, new_name:str=None, new_folder:str=None, new_link:str=None) -> None:
        item = self.get_item(name)
        if new_name:   item.name   = new_name
        if new_folder: item.folder = new_folder
        if new_link:   item.link   = new_link