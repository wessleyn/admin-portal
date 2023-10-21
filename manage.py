#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import shutil
from pathlib import Path
DIREC = Path(__file__).resolve().parent

def remove_pycache_and_migrations():
    for root, dirs, files in os.walk(directory):
        # Remove __pycache__ directories
        for dir_name in dirs:
            if dir_name == "__pycache__":
                dir_path = os.path.join(root, dir_name)
                shutil.rmtree(dir_path)
                print(f"Removed directory: {dir_path}")

        # Remove migration files
        for file_name in files:
            if file_name.endswith(".py") and file_name != "__init__.py":
                if "migrations" in root:
                    file_path = os.path.join(root, file_name)
                    os.remove(file_path)
                    print(f"Removed file: {file_path}")
            if file_name == 'db.sqlite3' and input('Are you sure you want to delete the database? Yes / No:\t').lower() in ['yes', 'y']:
                os.remove(file_name)

def custom_commands():
    
    if sys.argv[1] == 'rollback':
        if input('Are you sure you want to delete all pycache and migration? Yes / No:\t').lower() in ['yes','y' ]:
            remove_pycache_and_migrations()
        else:
            print('No changes to pycache and migration made')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal.settings.local')
    try:
        from django.core.management import execute_from_command_line
        custom_commands()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
