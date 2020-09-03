import pyperclip

def new_env(name, file = None):
    '''creates a new env with name and option from yml file'''

    string = 'conda create --name ' + str(name)
    if file != None:
        string = 'conda env create --name ' + str(name) + ' --file ' + str(file)

    print ('Copied to clipboard')
    pyperclip.copy(string)

def export_env(file):

    string = 'conda env export > ' + str(file)
    pyperclip.copy(string)

def remove_env(env):

    # note does not delete completely it just removes everything from the env
    string = 'conda remove --name ' + str(env) + ' --all'
    pyperclip.copy(string)
