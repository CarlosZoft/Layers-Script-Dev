import pyautogui
import os
import time
import subprocess
base_path = "/home/fael/layers/principais"
typeOfCommands = ['yarn start', 'docker-compose up']
paths = [
    "/tendaedu-web/web",
    "/tendaedu-web/app",
    "/layers-webapp",
    "/layers-auth-vanilla",
    "/tendaedu-backend/app",
]

# init docker in backend
command = "gnome-terminal --working-directory="+ base_path + "/tendaedu-backend" +" --tab -- bash -c '\
    "+ typeOfCommands[1] +";\
    exec bash'\
"
os.system(command)
 
# run apps
for i in paths:
    # sleeping for 2 seconds 
    time.sleep(2)
    command = "gnome-terminal --tab --working-directory="+ base_path + i +" -- bash -c '\
        sleep 5;\
        "+ typeOfCommands[0] +";\
        exec bash'\
    "
    os.system(command)
# feedback
print("all services running!")