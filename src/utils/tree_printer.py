import os


def print_directory_tree(root_dir, level=0):
    # Ignore directories starting with .
    negatives = ['venv', '.idea', '__pycache__', '.git']
    dirs = [d for d in os.listdir(root_dir) if d not in negatives]

    for i, d in enumerate(dirs):
        current_path = os.path.join(root_dir, d)
        if os.path.isdir(current_path):
            # Print current directory at the current level
            print('    ' * level + '|-- ' + d)
            # Recursively print subtree
            print_directory_tree(current_path, level + 1)
        else:
            # Print files
            print('    ' * level + '|-- ' + d)


# Example usage:
directory_path = '.'
print(f"Directory Tree of {directory_path}:")
print_directory_tree(directory_path)


# |-- requirements.txt
# |-- tests
#     |-- __init__.py
#     |-- utils
#         |-- __init__.py
#         |-- test_split_cron_command.py
#         |-- test_join_cron_command.py
# |-- README.md
# |-- .gitignore
# |-- scripts
#     |-- run_tests.sh
# |-- src
#     |-- __init__.py
#     |-- utils
#         |-- cron_command_parse.py
#         |-- __init__.py
#         |-- cron_manager.py
#         |-- TreePrinter.py
#     |-- setup.py
#     |-- gui
#         |-- launch.py
#         |-- frames.py
#         |-- DataViewModels.py
#         |-- dialogs.py
#     |-- main.py
