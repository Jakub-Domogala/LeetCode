#!/bin/bash

# prepared only to be run from repo root dir
python 4.utilities/readme_generator.py
git pull
git add .
git commit -m "$1"
git push
echo "Upload completed successfully!"
