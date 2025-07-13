#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./run_cpp.sh path/to/file.cpp"
  exit 1
fi

MAIN_FILE="$1"
EXEC="run_exec"

# Get the directory where the main file is located (e.g., "2.medium")
MAIN_DIR=$(dirname "$MAIN_FILE")

# Get the full path to the "utilities" directory at the same level, if it exists
UTIL_DIR="$MAIN_DIR/utilities"

# Collect all cpp files in that utilities directory
UTIL_CPP_FILES=""
if [ -d "$UTIL_DIR" ]; then
  UTIL_CPP_FILES=$(find "$UTIL_DIR" -name "*.cpp")
fi

# Compile main file and utility files
g++ -std=c++17 -Wall -Wextra "$MAIN_FILE" $UTIL_CPP_FILES -o "$EXEC"
if [ $? -ne 0 ]; then
  echo "❌ Compilation failed."
  exit 1
fi

# Run
echo "✅ Running..."
./"$EXEC"

# Clean up
rm -f "$EXEC"
