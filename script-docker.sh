#!/bin/bash
. ~/.nvm/nvm.sh

source ./config.sh 
path=$main_path
path+=$1

cd "$path"
docker-compose up -d