import argparse
from logging import ERROR
from src.logger import Logger

class Parser:
    def __init__(self, description=""):
        self.parser = argparse.ArgumentParser(description=description)

    def arguments(self):
        self.parser.add_argument(
            "-s", "--imagepath", required=False, help="Set original image path")
        self.parser.add_argument(
            "-i", "--logpath", required=False, help="Set log path")
        args = vars(self.parser.parse_args())

        args["imagepath"] = check_string("imagepath")
        args["logpath"] = check_string("logpath")

def check_string(name):
    if name != None and (name.isnumeric() or check_float(name)):
        print("L'argomento deve essere un intero: valore di default impostato")
        name = None
    return name

def check_float(potential_float):
    if potential_float == None:
        return False
    try:
        float(potential_float)
        return True
    except ValueError:
        return False