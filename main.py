import os
import time

path_scripts = "/home/fael/projects-helps-layers/script-for-run-services/"

map_directorys = [
    {
        "type": "docker", 
        "directory": "tendaedu-backend"
    },
    {
        "type": "yarn", 
        "directory": "tendaedu-backend"
    },
    {
        "type": "yarn", "directory": 
        "layers-auth-vanilla"
    },
    {
        "type": "yarn", 
        "directory": "layers-webapp"
    },
    {
        "type": "yarn", 
        "directory": "tendaedu-web/app"
    },
    {
        "type": "yarn", 
        "directory": "tendaedu-web/web"
    }
]

def type_service(type):
    if type == "docker":
        return "script-docker.sh"
    elif type == "yarn":
        return "script-yarn.sh"

def wait(seconds):
    time.sleep(seconds)

def run_service(typeOfScript, directory):
    command = f"gnome-terminal --tab -- bash {path_scripts}{typeOfScript} {directory}"
    os.system(command)
    

for i in map_directorys:
    print("prepare to run service: ", i["directory"])
    wait(2)
    run_service(type_service(i["type"]), i['directory'])
    