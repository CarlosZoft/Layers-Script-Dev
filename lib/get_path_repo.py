from lib import file_path
import os

def dist_find():
    if(os.path.isfile('main_path.txt') == False or os.path.getsize('main_path.txt') == 0):
        file_path.write_path('main_path.txt')
        while(input("this is correct full path of repositorys? (y/n) ") != 'y'):
            file_path.write_path('main_path.txt')
    else:
        with open('main_path.txt', 'r') as arquivo:
            path_repo = arquivo.read()
            while(input(f"do you want run this script in {path_repo}? (y/n) ") != 'y'):
                file_path.write_path('main_path.txt')
