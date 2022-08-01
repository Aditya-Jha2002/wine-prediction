from curses import raw
import os

dirs = [
    os.path.join("data","raw"),
    "data_given",
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

files_ = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init.py")
]

for file_ in files_:
    with open(file_, "w") as f:
        pass