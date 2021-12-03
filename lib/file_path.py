import os

def clear_path(file):
    with open(file, 'w') as arquivo:
        arquivo.write("")

def write_path(file):
    path_repo = input("Enter the path of the repositorys: ")
    if(path_repo[-1] != '/'):
        path_repo += '/'
    try:
        if(os.path.isdir(path_repo) == True):
            with open(file, 'w') as arquivo:
                arquivo.write(path_repo)
        else:
            raise Exception("The path is not a directory")
    except:
        print("The path is not valid")
        write_path(file)