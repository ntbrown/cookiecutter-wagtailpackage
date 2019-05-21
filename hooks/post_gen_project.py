"""
Does the following:
# 1. Removes the sandbox project if it isn't going to be used
"""

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_example_project(project_directory):
    """Remove the taskapp if celery isn't going to be used."""
    # Determine the local_setting_file_location
    location = os.path.join(
        PROJECT_DIRECTORY,
        'sandbox'
    )
    shutil.rmtree(location)


# 1. Removes the sandbox project if it isn't going to be used
if '{{ cookiecutter.create_example_project }}'.lower() == 'n':
    remove_example_project(PROJECT_DIRECTORY)
