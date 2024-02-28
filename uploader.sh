#!/bin/bash

# prepared only to be run from repo root dir
git checkout master
git pull
git add .
git commit -m "$1"
git push
python utilities/readme_generator.py
git checkout master
git pull
git add .
git commit -m "$1: Readme Updated at $(date +"%H:%M:%S %Y-%m-%d")"
git push
