#!/bin/bash
. ~/.nvm/nvm.sh

source ./config.sh 
path=$main_path
path+="tendaedu-web/web"

cd "$path"
nvm use
yarn start