#!/bin/bash

# prepared only to be run from repo root dir
git checkout master
git pull
git add .
git commit -m "$1"
git push
python 4.utilities/readme_generator.py
git checkout master
git pull
git add .
git commit -m "Readme Updated"
git push
