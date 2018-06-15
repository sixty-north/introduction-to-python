# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# For the workshop, you'll need to copy this into your WSGI configuration file.

import sys

# add your project directory to the sys.path
project_home = '_HOME_DIR_/introduction-to-python/v04/zaweb'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from zaweb import create_app
application = create_app()  # noqa
