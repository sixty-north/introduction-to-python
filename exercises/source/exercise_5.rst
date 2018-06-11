==================================
 Exercise 5: Zorkalike on the web
==================================

Now that we've got a nice, fully-functioning game written in Python, we need to
take the next obvious step: put it on the web. pythonanywhere makes it
relatively easy to host simple web servers written in Python, so we're going to
build a web server around ``zorkalike`` called ``zaweb``.

.. admonition:: Removing existing web apps

   If you're using the "beginner" subscription to pythonanywhere, you can only
   host one web app at a time. If you've created another one for some reason,
   you'll need to delete it before continuing this exercise.

5a: Create a new virtual environment
====================================

We'll install ``zaweb`` and its dependencies into a new virtual environment.
Create a new virtual environment named ``itp-web``::

  $ mkvirtualenv -p python3.5 itp-web

5b: Install ``zorkalike`` and ``zaweb`` into ``itp-web``
========================================================

Now we'll install both ``zorkalike`` and ``zaweb`` into this virtual environment:

.. code-block:: bash

   $ cd ~/introduction-to-python/v04/zorkalike
   $ pip install .
   $ cd ../zaweb
   $ pip install .

This will install both of these packages as well as their dependencies. These
dependencies are downloaded the `Python Package Index (PyPI)
<https://pypi.org/>`_.

5c: Create a pythonanywhere web app
===================================

Now we need to set up a new "web app" in pythonanywhere. In this step we'll
create the skeleton of the app, filling in the details in later steps.

Go to the "Web" tab in pythonanywhere and click "Add new web app" on the left.
Click "Next" on the first dialog, and then "manual configuration" on the next.
Select "Python 3.5" for your Python version, and then "Next" on the dialog after
that. You should now be on the configuration page for your app.

You need to tell the web app to use packages from our ``itp-web`` virtual
environment. Scroll down to the "Virtualenv" section and click on "Enter path to
a virtualenv, if desired". In the field it shows enter
"/home/<your-user>/.virtualenvs/itp-web".

5d: Set up the WSGI configuration for our service
=================================================

Web Server Gateway Interface (WSGI) is defined in the Python Enhancement
Proposal `PEP333 <https://www.python.org/dev/peps/pep-0333/>`_. It specifies a
common interface for the broad ecosystem of Python web servers, allowing them to
all be used through a single abstraction.

In this section you'll tell your pythonanywhere system how to use ``zaweb`` as a
WSGI server, thereby exposing it to the internet. Typically, as in this case, a
Python WSGI server will sit behind a more full-featured web server like nginx or
apache.

Copy your WSGI configuration file into the place where pythonanywhere expects
it. From your bash console run this command::

  cp ~/introduction-to-python/v04/zaweb/wsgi.py /var/www/<your-user>_pythonanywhere_com_wsgi.py

After this, go back to your "Web" tab and click the reload button.

Once this completes you should be able to point your browser at
https://<your-user>.pythonanywhere.com and play zorkalike!
