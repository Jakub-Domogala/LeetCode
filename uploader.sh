#!/bin/bash

# prepared only to be run from repo root dir
git checkout master
git pull
git add .
git commit -m "$1"
git push
if [[ "$OSTYPE" == "darwin"* ]]; then
    python3 utilities/readme_generator.py
elif [[ "$OSTYPE" == "cygwin" ]]; then
    python utilities/readme_generator.py
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
if [[ "$OSTYPE" == "darwin"* ]]; then
    python3 utilities/FileCounter.py
elif [[ "$OSTYPE" == "cygwin" ]]; then
    python utilities/FileCounter.py
elif [[ "$OSTYPE" == "msys" ]]; then
    python utilities/FileCounter.py
elif [[ "$OSTYPE" == "win32" ]]; then
    python utilities/FileCounter.py
else
    python3 utilities/FileCounter.py
fi
