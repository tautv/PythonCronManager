#!/bin/bash

if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    requirements_file="requirements_mac.txt"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Linux is not supported by this script."
    exit 1
elif [[ "$OSTYPE" == "cygwin" ]]; then
    # POSIX compatibility layer and Linux environment emulation for Windows
    requirements_file="requirements_win.txt"
elif [[ "$OSTYPE" == "msys" ]]; then
    # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
    requirements_file="requirements_win.txt"
elif [[ "$OSTYPE" == "win32" ]]; then
    # Windows
    requirements_file="requirements_win.txt"
else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi

echo "Installing dependencies from $requirements_file..."
pip install -r $requirements_file

echo "Dependencies installed successfully."
