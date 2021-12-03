#!/bin/bash
. ~/.nvm/nvm.sh

source ./config.sh 
path=$main_path
path+=$s1

use='false'
start='false'
docker='false'

while getopts ":nydp:" opt; do
    case $opt in
        n) use='true' ;;
        y) start='true';;
        d) docker='true';;
        p) path+="$2";;
    esac
done

echo "nvm use : $use"
echo "yarn start : $start"
echo "docker_start : $docker"
echo "path : $path"

cd "$path"

if [ $use = 'true' ]; then
    nvm use
    sleep 1
fi
if [ $start = 'true' ]; then
    yarn start
    sleep 1
fi
if [ $docker = 'true' ]; then
    docker-compose up -d
    sleep 1
fi