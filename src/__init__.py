# insert boilerplate workaround courtesy of stack overflow
# source: https://stackoverflow.com/a/61079434
from os import path
import sys

project_directory = path.abspath('./notebooks')
project_path = path.dirname(project_directory)

if not project_path in sys.path:
    sys.path.append(project_path)