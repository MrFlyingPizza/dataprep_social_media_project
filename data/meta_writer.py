from os import listdir
from os.path import isfile, join
import json

"""
Responsible for generating the meta file
"""

_metapath_ = "data/meta.json"
_tablepath_ = "data/tables"

def getTables(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    return files

def writeMeta(path):
    tables = getTables(path)

    print("Writing meta file with following tables: ")
    for t in tables:
        print("\t"+t)

    with open(_metapath_, "w") as save_file:
        json.dump({"tables" : tables}, save_file, sort_keys=True, indent=4)

if __name__ == "__main__":
    writeMeta(_tablepath_)



