#!/bin/bash

# Remove the build folder if it exists
if [ -d "build" ]; then
    echo "Removing build directory..."
    rm -rf build
fi

# Remove the dist/mac folder if it exists
if [ -d "dist/mac" ]; then
    echo "Removing dist/mac directory..."
    rm -rf dist/mac
fi

# Run py2exe to build the project
echo "Running py2app..."
python setup.py py2app
echo "Build completed."
open "."
