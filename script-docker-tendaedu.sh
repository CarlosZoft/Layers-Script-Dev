#!/bin/bash
. ~/.nvm/nvm.sh

source ./config.sh 
path=$main_path
path+="tendaedu-backend"

cd "$path"
docker-compose up -d