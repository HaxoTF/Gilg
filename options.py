import os
import folders as folds
import json
from typing import Literal, Dict

file_path = folds.get_fold("Gilg/user_settings.json")
ValueType = Literal["text", "number", "precise", "switch", "any"]
browsers = ["chrome", "chromium", "edge", "firefox", "opera", "vivaldi", "brave"]

type_map = {
    "text"    : str,
    "number"  : int,
    "precise" : float,
    "switch"  : bool
}

class ValueNotAllowed(Exception): ...
class TypeNotAllowed(Exception): ...

class Option:
    def __init__(self, name:str, value, value_type:ValueType="any", allowed:list=None) -> None:
        self.name = name
        self.value_type :ValueType = value_type
        self.allowed = allowed
        self.value = None
        
        self.set_value(value)
    
    def set_value(self, value) -> None:

        if self.value_type != "any":
            if not isinstance(value, type_map[self.value_type]):
                raise TypeNotAllowed
        
        if self.allowed:
            if value not in self.allowed:
                raise ValueNotAllowed
        
        self.value = value
    
    def to_dict(self) -> Dict:
        return {
            "name" : self.name,
            "value" : self.value
        }
    
    def from_dict(self, data:Dict) -> None:
        self.name = data["name"]
        self.value = data["value"]

defaults = {
    Option("browser", browsers[0], "text", browsers)
}

class OptDrawer:
    def __init__(self) -> None:
        self.options :list[Option] = defaults
        if os.path.exists(file_path): self.load()
    
    def get_opt(self, name:str) -> Option:
        for opt in self.options:
            if opt.name == name:
                return opt
    
    def load(self):
        with open(file_path, "r") as f:
            data = json.load(f)
        
        for d in data:
            opt = self.get_opt(d["name"])
            if opt: opt.from_dict(d)

    def save(self):
        data :list[Dict] = []

        for opt in self.options:
            data.append(opt.to_dict())
        
        with open(file_path, "w") as f:
            json.dump(data, f)