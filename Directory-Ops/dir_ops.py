import shutil
import pyperclip
import os
import sys

backslash = '\\'

def get_cwd():
    '''returns current working directory'''
    return os.getcwd()

def cd_dot_dot(path):
    '''goes back one level in the path'''

    path_list = path.split(backslash)
    back_one = join_dirs(path_list[:-1])
    return back_one

def list_contents(path):
    '''shows all directories and files contained in path'''

    return os.listdir(path)

def path_exists(path):
    '''returns boolean checking is path exists'''

    return os.path.exists(path)

def join_dirs(list_of_items):
    '''joins directories with a backslash in between'''

    return backslash.join(list_of_items)

def copy_paste_file(copy_path, paste_path):
    '''copies and pastes a file into a new location'''

    print (copy_path)
    print (paste_path)

    if path_exists(copy_path) and not path_exists(paste_path):
        shutil.copyfile(copy_path, paste_path)
        print ('copying file...')


def remove_file(path, override = False):
    '''removes file at given path'''

    inp = 'delete'
    if not override:
        inp = input('Type "delete" to delete ' + str(path) + ': ')

    if inp == 'delete':
        if path_exists(path):
            os.remove(path)

def rename_file(og_path, new_path):
    '''renames og to new'''

    if path_exists(og_path) and not path_exists(new_path):
        os.rename(og_path, new_path)

def create_dir(path):
    '''creates a directory at path'''

    if not path_exists(path):
        os.mkdir(path)




if __name__ == '__main__':
    cd = get_cwd()
