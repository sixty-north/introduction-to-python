=============================
 Exercise 3: Python packages
=============================

So far you've done all of your work in a single file, ``zorkalike.py``. This
works, but as your program gets larger you'll want to break it up into multiple
files. Python calls these files *modules*, and --- loosely speaking --- a
*package* is a collection of modules.

In this exercise we'll move our work into a new arrangement with multiple files.

3a: Move ``KazooRoom`` into a new module
========================================

So far you're work has been in ``v01/zorkalike.py``. We're going to move your
work over to the directory structure in ``v03``. Take your class ``KazooRoom``
and put it into ``v03/zorkalike/rooms/kazoo_room.py``.

Note that this is a fairly mechanical change, but this is all you need to do to
make your module part of the ``zorkalike`` package (which is rooted at
``v03/zorkalike``).

Notice that ``KazooRoom``\ 's base class, ``Room``, is now defined in a different
module than ``KazooRoom``. Look at other room implementations to see how to
*import* ``Room`` into the ``KazooRoom`` implementation.

3b: Update ``make_game()``
==========================

In exercise 2 you modified the function ``make_game()`` to include a kazoo room.
Locate this function in the ``v03/zorkalike`` package and make the same
modification.

Since ``KazooRoom`` is now defined in a different module than ``make_game``
you'll need to *import* it. See how other rooms are imported and follow that
pattern for ``KazooRoom``.

Use this opportunity to look at the overall structure of the package. Does this
structure seem reasonable to you? What are those Python files with the funny
names?

3c: Update ``BearRoom``
=======================

The last thing we changed in exercise 2 was to update ``BearRoom`` such that the
kazoo soothed the bear. Locate ``BearRoom`` in the ``v03/zorkalike`` package and
make the same modification.

3d: Run the game!
=================

Now that you've moved all of your changes in a proper Python package, let's run
the game! From the bash console (either an existing or new one) run this:

.. code-block:: bash

   $ cd ~/introduction-to-python/v03
   $ python3 -m zorkalike

Verify that the game works with your changes.
