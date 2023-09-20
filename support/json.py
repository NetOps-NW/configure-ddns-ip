
from support.logger import logger;
import json;
import os;

def from_json(path="", str=""):
    if path:
        if os.path.exists(path):
            with open(path, "r") as file:
                return json.load(file);
        else:
            logger.error(f"Path {path} doesn't exist.");
    else:
        return json.loads(str);

def to_json(object=dict(), path=""):
    if path:
        with open(path, "w") as file:
            json.dump(object, file, indent=4);
    else:
        return json.dumps(object, indent=4);
        