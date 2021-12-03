#!/bin/bash
. ~/.nvm/nvm.sh

source ./config.sh 
path=$main_path
path+="layers-webapp"

cd "$path"
nvm use
yarn start