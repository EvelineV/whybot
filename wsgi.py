import sys

# Working WSGI file for PythonAnywhere.com

path = '/home/your_username/whybot'
if path not in sys.path:
    sys.path.append(path)
from why_api import api as application
