#!/bin/bash

# prepared only to be run from repo root dir
git checkout master
git pull
git add .
git commit -m "$1"
git push
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Running on Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    python3 utilities/readme_generator.py
elif [[ "$OSTYPE" == "cygwin" ]]; then
    echo "Running on Windows/Cygwin"
elif [[ "$OSTYPE" == "msys" ]]; then
    python utilities/readme_generator.py
elif [[ "$OSTYPE" == "win32" ]]; then
    python utilities/readme_generator.py
else
    python3 utilities/readme_generator.py
fi
git checkout master
git pull
git add .
git commit -m "$1: Readme Updated at $(date +"%H:%M:%S %Y-%m-%d")"
git push
