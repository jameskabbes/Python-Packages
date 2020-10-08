###importing folders and files

def import_func():

    import sys
    sys.path.append('C:/Users/e150445/Documents/Python-Packages')
    import import_packages as imp
    imp.package_import()

def package_import():

    import os
    import sys

    backlash = '\\'

    #Get Folder
    path_list = __file__.split(backlash)
    folder = backlash.join(path_list[:-1])

    ###Get Subfolders
    subfolders = os.listdir(folder)

    ### Add to path
    i = 1
    for sub in subfolders:
        new = folder + '/' + sub
        sys.path.append(new)
        print ('Importing (' + str(i) + '/' + str(len(subfolders)) + ')...', end = '\r')
    print('Import Complete')

if __name__ == '__main__':
    package_import()
