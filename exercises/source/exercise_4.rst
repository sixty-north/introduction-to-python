==================================
 Exercise 4: Virtual environments
==================================

In Python, a *virtual environment* is an isolated copy of an existing Python
installation, e.g. your system Python. These are cheap to make and destroy, and
they let you install the specific dependencies you need without worrying about
polluting other Python environments.

In this exercise we'll create a new virtual environment, install our
``zorkalike`` package into it, and see that we can run our program from anywhere
in the system.

.. admonition:: virtualenvwrapper

   The Python standard library provides the basic support for virtual
   environment via the `venv <https://docs.python.org/3/library/venv.html>`_
   package. While everything we describe in this exercise can be done using
   ``venv`` directly, we're going to use a higher-level tool called
   `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`_
   that simplifies the use of virtual environments.

   ``virtualenvwrapper`` is very widely used, and it's installed by default in
   your pythonanywhere shell environment. In particular, it provides the
   ``mkvirtualenv`` and ``workon`` commands you'll see below.


4a: Create a new virtual environment
====================================

Before you can use a virtual environment you must first create it. To do this you need to specify two things:

1. The name of the virtual environment
2. The existing Python environment (it would be another virtual environment) to
   copy from

We'll create our environment using the Python 3.5 installation on
pythonanywhere, and we'll call it "itp" (short for "introduction to python"). In your bash console, run these commands:

.. code-block:: bash

   $ cd ~/introduction-to-python/v03
   $ mkvirtualenv -p python3 itp

After a few seconds it should say "done" and show you a prompt like this::

    (itp) 13:02 ~/introduction-to-python/v03 (master)$

The "(itp)" at the front of the line is the name of the virtual environment.
Bash on this system (and on many systems these days) is configured to display
the active virtual environment like this.

4b: Deactivate and reactivate the virtual environment
=====================================================

When you created your virtual environment is was automatically *activated* for
you. When an environment is active, the command "python" on the command line
will refer to the Python executable for your environment. It will have access to
the modules specifically installed in your environment.

In this exercise you're going to deactivate and reactivate your virtual
environment. In the same bash shell as the previous section, run this command:

.. code-block:: bash

   $ deactivate

You should see your prompt turn to something like this::

  13:43 ~/introduction-to-python/v03 (master)$

The virtual environment indicator at the front of the prompt is gone. The
command ``which python3`` will show that you're now using the system Python
installation.

Now reactivate your environment::

  $ workon itp

You'll see that your prompt is restored and that ``which python3`` shows that
you're using the Python in your virtual environment.

4c: Install ``zorkalike`` into your virtual environment
=======================================================

Our ``zorkalike`` package comes with a script called ``setup.py``. This script
describes how to install our package into a Python environment like the one
you've just created, so let's do that. Go to the bash console you've been using and run these commands:

.. code-block:: bash

   $ workon itp
   $ cd ~/introduction-to-python/v03
   $ pip install .

After a few seconds this will finish. From your bash console ``cd`` to your home
directory and start a Python REPL like this:

.. code-block:: bash

   $ cd
   $ python3

This will start Python and take you to the ``>>>`` prompt. At this prompt run these commands:

.. code-block:: pycon

   >>> import zorkalike
   >>> zorkalike.__file__
   '/home/<your-name>/.virtualenvs/itp/lib/python3.5/site-packages/zorkalike/__init__.py'

This demonstrates that Python is importing the module from your virtual
environment, even though you started Python from a location completely
dissociated with your project. This is what we want! Type ``ctrl-d`` to exit Python.

4d: Play the game
=================

Another thing that ``setup.py`` did for us was to create a top-level program for
``zorkalike``. That is, it installed a program called ``zorkalike`` that calls
the "main" function in your package. Using the same bash console as the last
step, let's now run the program ``zorkalike``::

  $ zorkalike

If everything went smoothly, you should be playing your game.
