#!/bin/bash
. ~/.nvm/nvm.sh

source ./config.sh 
path=$main_path
path+="layers-auth-vanilla"

cd "$path"
nvm use
yarn start