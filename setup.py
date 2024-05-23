from setuptools import setup
import sys
import os

# Create necessary directories if they don't exist
dist_dir = 'dist/win' if sys.platform.startswith('win') else 'dist/mac'
if not os.path.exists(dist_dir):
    os.makedirs(dist_dir)

# Common dependencies
common_deps = [
    'wxPython',
    # other common dependencies
]

# Windows-specific setup
if sys.platform.startswith('win'):
    import py2exe
    extra_deps = ['py2exe']
    options = {
        'py2exe': {
            'packages': ['wx'],  # Include wxPython package
            'dist_dir': 'dist/win',  # specify the output directory as dist/win for py2exe
            'bundle_files': 1,  # Bundles everything into a single executable
            'compressed': True,  # Compresses the library archive into the exe
        }
    }
    setup(
        name='PythonCronManager',
        version='0.1.0',
        windows=[{
            'script': 'src/main.py',
            'icon_resources': [(1, 'src/images/icon.ico')]
        }],
        options=options,
        install_requires=common_deps + extra_deps,
        zipfile=None,  # Indicates that the library archive should be included in the executable
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
        version='0.0.1',
        app=['src/main.py'],
        options=options,
        install_requires=common_deps + extra_deps,
        setup_requires=['py2app'],
    )

else:
    print("Unsupported platform")
