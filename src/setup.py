from setuptools import setup, find_packages

setup(
    name='PythonCronManager',
    version='1.0.0',
    description='A Python Cron Manager application',
    author='tautv',
    url='https://github.com/tautv/PythonCronManager',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'PythonCronManager = main:main'
        ]
    },
    install_requires=[
        # Add your dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)