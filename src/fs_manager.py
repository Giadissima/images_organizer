from os.path import exists, dirname
from os import makedirs

def create_folder_if_not_exist(file_path):
    directory = dirname(file_path)  
    if not exists(directory):
        makedirs(directory)

def create_file_if_not_exist(file_path):
    create_folder_if_not_exist(file_path)
    with open(file_path, 'w'): pass
