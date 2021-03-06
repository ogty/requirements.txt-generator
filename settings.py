import json
import os
import platform


os_name = platform.system()
if os_name == "Darwin" or os_name == "Linux":
    DESKTOP_PATH = os.path.join(os.path.join(os.environ["HOME"]), "Desktop")
elif os_name == "Windows":
    DESKTOP_PATH = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")

PATH_SPLIT_WORD = "\\" if os_name == "Windows" else "/"

TOP_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.join(TOP_DIR, "src")
STATIC_DIR = os.path.join(TOP_DIR, "static")
TREE_PATH = os.path.join(STATIC_DIR, "tree.json")

with open(os.path.join(STATIC_DIR, "config.json"), "r") as config_file:
    CONFIG = json.load(config_file)

IGNORE_DIRECTORIES = CONFIG["ignores"]
