============================
 Exercise 1: Workshop setup
============================

1a: Create a "beginner" account on pythonanywhere.com
=====================================================

`pythonanywhere.com <pythonanywhere.com>`_ is a hosted Python environment. It
gives you access to Python shells, basic tools like ``bash`` and ``git``, plus an
editor and filesystem. We'll be using pythonanywhere to do the exercises in the
workshop.

So the first thing you need to do is create a pythonanywhere account. The
"beginner" account is free and more than sufficient for this workshop. You can
`create your new account here
<https://www.pythonanywhere.com/registration/register/beginner/>`_.

1b: Clone the workshop material
===============================

This workshops is built around an existing body of code for the ``zorkalike``
project. You need to use ``git`` to clone that material into your workspace. On
pythonanywhere, go to your *Dashboard*. From there, under "New Console" click
the button labeled "$ Bash"; this will open up a new bash shell. You'll be
presented with a prompt something like this::

   09:46 ~$

.. note::

  Note that this shell will stay running even if you navigate away from it. You
  can use the same shell for the entire workshop, or you destroy/create them as
  you want.

At this prompt, run this command to clone the repository:

.. code-block:: bash

   $ git clone https://github.com/sixty-north/introduction-to-python

.. note::

   When we show shell commands like this we'll prefix them with ``$``. This
   punctuation is **not** part of what you type; it merely indicates the prompt.
   This allows us to visually disinguish commands from their output which is not
   prefixed with ``$``.

This will create a directory named ``introduction-to-python``. You can navigate to
that directory and see that its contents look like this:

.. code-block:: bash

   $ cd introduction-to-python
   $ ls
   README.rst  cold-start  exercises notebooks  requirements.txt  test  v01  v02  v03  v04

If this looks correct, then you should be ready for the rest of the workshop!
