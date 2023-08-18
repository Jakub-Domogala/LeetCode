#!/bin/bash


# Run generate.py
python readme_generator.py

# Git pull to get the latest changes
git pull

# Add all changes to the staging area
git add .

# Commit with the provided argument as the commit message
git commit -m "$1"

# Push the changes to the remote repository
git push

echo "Upload completed successfully!"
