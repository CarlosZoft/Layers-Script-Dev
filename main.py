from lib import methods
from lib import repositorys
from lib import get_path_repo
import os

get_path_repo.dist_find()
path_script = os.path.dirname(os.path.abspath(__file__)) + '/script.sh'

addApps = input("Do you want to add apps to running? (y/n): ")

# List of apps available
for idUnique, app in enumerate(repositorys.apps.keys()):
    print(f"\n{idUnique} - {app}")

# Select apps to run
selectedApps = input(f"\nselect the apps with format : '0,1,2':\n");

# Running default repositorys
for i in repositorys.data:
    print(f"prepare to run {i['type']} on {i['directory']}")
    methods.wait(5)
    methods.run_service(path_script, i['directory'], i['flag'])

# Running apps
def run_app(currentRepo, relativePath ):
    path = currentRepo[relativePath]
    print(f"prepare to run {relativePath} on {path['directory']}")
    methods.run_service(path_script, path["directory"], path["flag"])
    methods.wait(5)

# Worker selected apps
for i in selectedApps.split(','):  
    indexOfApp = int(i)
    listOfApps = list(repositorys.apps.keys())
    if(indexOfApp < len(listOfApps)):
        key = listOfApps[int(indexOfApp)]
        # if have docker, run it
        if(key in repositorys.docker.keys()):
            run_app(repositorys.docker[key], 'docker')
        #  if have interface, run it
        if("interface" in repositorys.apps[key]):
            run_app(repositorys.apps[key],"interface")
        # if run backend, run it
        if("backend" in repositorys.apps[key]):
            run_app(repositorys.apps[key],"backend")
    else :
        print("Not possible run the app with id :", indexOfApp)