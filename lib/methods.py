import os
import time

def wait(seconds):
    time.sleep(seconds)

def run_service(path_script, directory, flags):
    command = f"gnome-terminal --tab -- bash {path_script} -p {directory} {flags}"
    os.system(command)