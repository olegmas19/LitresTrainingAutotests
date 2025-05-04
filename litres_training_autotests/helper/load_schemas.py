import json
import os


CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
SCHEMA_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "schemas")


def load_schema(filename):
    with open(SCHEMA_DIR + f"{filename}") as file:
        schema = json.load(file)
        return schema
