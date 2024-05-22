from setuptools import setup
import sys
import py2app

APP = ['src/main.py']  # Change 'main.py' to your main script
DATA_FILES = []

OPTIONS = {
    'argv_emulation': True,
    'packages': ['wx'],  # Include wxPython package
    # 'includes': ['wx'],  # Use if needed to explicitly include other modules
}

setup(
    name='PythonCronManager',
    version='0.01',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    install_requires=[
        'wxPython',
        # Other dependencies
    ],
)
