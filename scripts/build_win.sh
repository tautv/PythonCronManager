#!/bin/bash

# Remove the build folder if it exists
if [ -d "build" ]; then
    echo "Removing build directory..."
    rm -rf build
fi

# Remove the dist/win folder if it exists
if [ -d "dist/win" ]; then
    echo "Removing dist/win directory..."
    rm -rf dist/win
fi

# Run py2exe to build the project
echo "Running py2exe..."
python setup.py py2exe

echo "Build completed."

explorer.exe "."
