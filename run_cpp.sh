#!/bin/bash

# Ensure a file path is provided
if [ -z "$1" ]; then
  echo "Usage: ./run_cpp.sh path/to/filename.cpp"
  exit 1
fi

FILE="$1"

# Check if file exists
if [ ! -f "$FILE" ]; then
  echo "Error: File '$FILE' not found."
  exit 1
fi

# Extract filename without extension and directory
FILENAME=$(basename -- "$FILE")
EXEC="${FILENAME%.*}_exec"

# Compile
g++ -std=c++17 -Wall -Wextra -O2 "$FILE" -o "$EXEC"
if [ $? -ne 0 ]; then
  echo "❌ Compilation failed."
  exit 1
fi

# Run
echo "✅ Running..."
./"$EXEC"

# Clean up
rm -f "$EXEC"
