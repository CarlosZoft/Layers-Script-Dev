from lib import methods
from lib import repositorys
from lib import get_path_repo
import os

get_path_repo.dist_find()

path_script = os.path.dirname(os.path.abspath(__file__)) + '/script.sh'
    
for i in repositorys.data:
    print("prepare to run service: ", i["directory"])
    methods.wait(5)
    methods.run_service(path_script, i['directory'], i['flag'])
    