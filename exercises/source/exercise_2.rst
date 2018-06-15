=============================
 Exercise 2: Soothe the bear
=============================

The goal of this exercise will be to create a new type of room. In this room
there will be an object that, if the player uses it, will allow them to survive
petting the bear.

Python dictionaries
===================

For this exercise you'll need to do some work with Python dictionaries. These
are used extensively throughout the code and, indeed, throughout most Python
code in the world. For example, we use dictionaries to model room contents,
player inventory, and doors between rooms. Here's a quick introduction to
dictionaries.

You can create dictionaries with the ``{key: value, . . .}`` syntax. For
example, to create a new dictionary mapping the word "apple" to the word "red",
you would use:

.. code-block:: python

   x = {'apple': 'red'}

You can access elements in a dictionary by key using the ``[]`` operator. So to
get the value in a dictionary with the key "apple", you would use:

.. code-block:: python

   x['apple']

Similarly, you can set values in a dictionary with the same syntax. So to map
"apple" to "green" you would use:

.. code-block:: python

   x['apple'] = 'green'

You can add new key-value mappings in the same way:

.. code-block:: python

   x['banana'] = 'yellow'

You can check if a key is in a dictionary using the ``in`` keyword:

.. code-block:: python

   if 'banana' in x:
       print('there is a banana')

Likewise, you can check if a key is *not* in a dictionary usinst ``not in``:

.. code-block:: python

   if 'apple' not in x:
       print('there is no apple')

That's a *very* quick overview of dictionaries in Python, but it should be
enough for this workshop.

1a: Create a new type of room
=============================

Your first task is to create a new type of room, the ``KazooRoom``. This room
will contain a kazoo that the player can pick up.

For this task you should edit the file ``v01/zorkalike.py``.

This task will involve a few elements:

- Create a new ``Room`` subclass
- Initialize new ``KazooRoom`` instances with contents (i.e. one kazoo)
- The room description should indicate if it has any kazoos
- The room's ``process_command()`` should allow the user to "take kazoo" if there
  is a kazoo available. Taking the kazoo should a) add it to the player's
  inventory and b) remove it from the room's contents.

Whoa! Slow down!!!
------------------

If you don't know Python then this may sound daunting! Remember that the point
of this workshop is not to "learn Python". Rather, we want you to get a sense
for how programming with Python *feels*. Don't be afraid to look at the
solutions we've provided. Try to understand what's been done in broad strokes
rather than all the details of every line of code.

2b: Add a ``KazooRoom`` to the game
===================================

Now that you've created a new room type, let's add it to the game. Modify the
function ``make_game()`` so that there's a ``KazooRoom`` to the west of the
starting room.

This work should continue in ``v01/zorkalike.py``.

Once you've got this in place you should run your game. Go to a bash console and
run:

.. code-block:: bash

   $ cd ~/introduction-to-python/v01
   $ python3 zorkalike.py

If you go west from the start room you'll be in your new room. Take that kazoo!

2c: Play the kazoo, calm the bear
=================================

As we all know, kazoo music is the best way to soothe an angry bear. In this
task, we'll update the ``BearRoom`` so that playing the kazoo will calm the
bear, allowing you to safely pet it.

This is no small task. We need to change ``BearRoom``\ 's base class, implement
a ``description`` function, model the bear's demeanor, and handle the "play
kazoo" command. Let's break that down into implementable bites:

- Change the ``BearRoom`` base class from ``StaticRoom`` to ``Room``.
- Use ``BearRoom.contents`` to hold information about the bear's demeanor. It
  starts angry but will be calmed by dulcet kazoo melodies.
- Add the ``description`` property to ``BearRoom``. It should return a string
  describing the bear's demeanor.
- Update ``BearRoom.process_command`` to support the "play kazoo" command. If
  the player does this and they don't have a kazoo, it should say so. If they do
  have a kazoo, the bear should become calm.
- Update ``BearRoom.process_command`` so that "pet bear" for a calm bear doesn't
  result in the player's tragic death.

Do all of this work in ``v01/zorkalike.py``.

As before, this is a lot to do. Don't hesitate to look at the solution for
guidance.
