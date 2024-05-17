import os
import re


def get_setup_content():
    setup_path = os.path.join(os.path.dirname(__file__), '..', 'setup.py')
    with open(setup_path, 'r') as f:
        setup_content = f.read()
    return setup_content


def get_version():
    setup_content = get_setup_content()
    version_match = re.search(r"version=['\"]([^'\"]+)['\"]", setup_content)
    if version_match:
        return version_match.group(1)
    else:
        raise ValueError("Version not found in setup.py")


def get_name():
    setup_content = get_setup_content()
    name_match = re.search(r"name=['\"]([^'\"]+)['\"]", setup_content)
    if name_match:
        return name_match.group(1)
    else:
        raise ValueError("Name not found in setup.py")


def get_description():
    setup_content = get_setup_content()
    description_match = re.search(r"description=['\"]([^'\"]+)['\"]", setup_content)
    if description_match:
        return description_match.group(1)
    else:
        raise ValueError("Description not found in setup.py")
