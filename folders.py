import os

root = os.getenv("APPDATA")

fold_base = [
    "Gilg",
    "Gilg/packs"
]

def prep_folds() -> None:
    for fold in fold_base:
        full_path = os.path.join(root, fold)
        if not os.path.exists(full_path):
            os.mkdir(full_path)

def get_fold(path:str) -> str:
    return os.path.normpath(os.path.join(root, path))

def get_data_location() -> str:
    return os.path.join(root, fold_base[0])

def count_files(path:str):
    result = 0
    for root, dirs, files in os.walk(path):
        result += len(files)
    return result