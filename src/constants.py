from src.parser import Parser
from os.path import join

def check_if_arg(name, args, default):
    if args != None and args[name] != None:
        return args[name]
    return default

parser = Parser()
args = parser.arguments()

# constants
IMAGE_PATH = check_if_arg("imagepath", args, "src/images")
LOG_PATH = check_if_arg("logpath", args, "log")
DEBUG_LOG = join(LOG_PATH, "debug.log")
ERROR_LOG = join(LOG_PATH, "error.log")
