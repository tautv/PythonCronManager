from setuptools import setup
import sys

# Common dependencies
common_deps = [
    'wxPython',
    # other common dependencies
]

# Windows-specific setup
if sys.platform.startswith('win'):
    extra_deps = ['py2exe']
    options = {
        'py2exe': {
            'packages': ['wx'],  # Include wxPython package
            'dist_dir': 'dist/win',  # specify the output directory as dist/win for py2exe
            'icon_resources': [1, 'src/images/icon.ico']
        }
    }
    setup(
        name='PythonCronManager',
        version='0.01',
        windows=[{'script': 'src/main.py'}],
        options=options,
        install_requires=common_deps + extra_deps,
    )

# macOS-specific setup
elif sys.platform.startswith('darwin'):
    extra_deps = ['py2app']
    options = {
        'py2app': {
            'packages': ['wx'],  # Include wxPython package
            'dist_dir': 'dist/mac',  # specify the output directory as dist/mac for py2app
            'iconfile': 'src/images/icon.icns'
        }
    }
    setup(
        name='PythonCronManager',
        version='0.01',
        app=['src/main.py'],
        options=options,
        install_requires=common_deps + extra_deps,
        setup_requires=['py2app'],
    )

else:
    print("Unsupported platform")
