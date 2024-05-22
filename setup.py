from setuptools import setup
import sys
import py2exe

# Common dependencies
common_deps = [
    'wxPython',
    # other common dependencies
]

# Windows-specific setup
if sys.platform.startswith('win'):
    extra_deps = ['py2exe']
else:  # macOS-specific setup
    extra_deps = ['py2app']

setup(
    name='PythonCronManager',
    version='0.01',
    windows=[{'script': 'src/main.py'}] if sys.platform.startswith('win') else None,
    app=['src/main.py'] if sys.platform.startswith('darwin') else None,
    options={
        'py2exe': {
            'packages': ['wx'],  # Include wxPython package
        },
        'py2app': {
            'packages': ['wx'],  # Include wxPython package
        }
    },
    install_requires=common_deps + extra_deps,
)
