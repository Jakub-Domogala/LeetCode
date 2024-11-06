#!/bin/bash

# Check if an argument was provided
if [ -z "$1" ]; then
  echo "Usage: ./upload_task <file_prefix>"
  exit 1
fi

# Define the file prefix to search for
file_prefix="$1"

# Find the file starting with the prefix, searching recursively from the current directory
file_path=$(find . -type f -name "${file_prefix}. *py" | head -n 1)

# Check if the file was found
if [ -z "$file_path" ]; then
  echo "File starting with ${file_prefix} not found."
  exit 1
fi

# Upload the file (replace 'upload_command' with the actual command)
echo "$file_path" # Replace with your actual upload command, e.g., `scp`, `rsync`, etc.

echo "File ${file_path} uploaded successfully."


#!/bin/bash

# prepared only to be run from repo root dir
git checkout master
git pull
git add "$file_path"
git commit -m "$file_prefix"
git push
