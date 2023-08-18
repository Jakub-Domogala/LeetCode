#!/bin/bash

if [ "$1" == "upload" ] && [ "$2" ]; then
    # Run generate.py
    python generate.py

    # Git pull to get the latest changes
    git pull origin main

    # Add all changes to the staging area
    git add .

    # Commit with the provided argument as the commit message
    git commit -m "$2"

    # Push the changes to the remote repository
    git push origin main

    echo "Upload completed successfully!"
else
    echo "Usage: $0 upload 'commit message'"
fi
