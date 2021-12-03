#!/bin/bash
. ~/.nvm/nvm.sh

source ./config.sh 
path=$main_path
path+="tendaedu-web/app"

cd "$path"
nvm use
yarn start