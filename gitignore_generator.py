#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

import os
import sys

if len(sys.argv) == 5:
    drive, workspace_name, project_name, language = sys.argv[1:]
else:
    drive = input("Enter drive: ")
    workspace_name = input("Enter workspace: ")
    project_name = input("Enter project_name: ")
    language = input("Enter programming language: ")

os.chdir("{}:/".format(drive.upper()))

languages = {
  "python": [".idea/", "venv/", "resources/"],
  "spring": ["idea/", "target/"],
  "java": ["idea/", "out/"],
}


def search_workspace():
    for directories in os.walk("."):
        for directory in [directory for directory in directories if directory.__contains__(workspace_name)]:
            for folder in [folder for folder in directory if folder == workspace_name]:
                return os.path.join(os.getcwd(), folder)


def search_project(parent):
    for folder in [folder for folder in os.listdir(parent) if folder == project_name]:
        return os.path.join(parent, folder)


def get_gitignore_list():
    language_type = languages.get(language)
    if language is None:
        return None
    return language_type


def write_gitignore_file():
    if get_gitignore_list() is not None:
        workspace_path = search_workspace()
        target_abs_path = search_project(workspace_path)
        with open(r"{}/.gitignore".format(target_abs_path), "w") as gitignore_file:
            gitignore_file.writelines('\n'.join(get_gitignore_list()))
            print("Created .gitignore in {}".format(target_abs_path))
    else:
        print("Unable to generate .gitignore")


write_gitignore_file()
