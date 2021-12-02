import os
import time
import subprocess
base_path = "~/layers/principais"
paths = [
    "/tendaedu-backend/app",
    "/layers-auth-vanilla",
    "/layers-webapp",
    "/tendaedu-web/app",
    "/tendaedu-web/web",
]
#subprocess.call('gnome-terminal --tab --', shell = True)
# command = "gnome-terminal -- /bin/sh -c 'cd "+ base_path + paths[0] +";sleep 2;yarn start;exec bash'"
# os.system(command)

for i in paths:
    command = "gnome-terminal -- /bin/sh -c 'cd "+ base_path + i +";sleep 3;yarn start;exec bash'"
    os.system(command)
    time.sleep(7)