import os
import time

path_scripts = "/home/fael/projects-helps-layers/script-for-run-services/"
map = [
    "script-docker-tendaedu.sh",
    "script-tendaedu.sh",
    "script-auth-vanilla.sh",
    "script-tendaedu-web-web.sh",
    "script-tendaedu-web-app.sh",
    "script-layers-webapp.sh"
]

for i in map:
    time.sleep(3)
    command = f"gnome-terminal --tab -- bash {path_scripts}{i}"
    os.system(command)