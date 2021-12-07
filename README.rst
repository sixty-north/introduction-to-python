|Python version| |Build Status|

========================
 Introduction to Python
========================

Supporting material for our "Introduction to Python" talk.

Dependencies
============

To install the depencies for the talk::

    pip install -r requirements.txt

Tests
=====

To run the (very basic) smoke tests, do this::

    cd test
    ./run-tests.sh

This simulates a run through the game for each of the available implementation
to make sure they aren't diverging.

Presentation
============

Setup
-----

* Create virtualenv for jupyter
* Run jupyter in that venv. Open the webpage in a standalone browser for presentation.
* Bring up slides in keynote.
* Bring up IDE

Order
-----

1. Cold start. Talk through cellular automata
2. Jupyter notebook: Zorkalike
3. Code v01: Same as in Zorkalike, but in files
4. Code v02: Restructured into multiple files
5. Code v03: As a proper package.
6. Code v04: With a web frontend
7. Jupyter notebook: Matplotlib


.. |Python version| image:: https://img.shields.io/badge/Python_version-3.6+-blue.svg
   :target: https://www.python.org/
.. |Build Status| image:: https://travis-ci.org/sixty-north/introduction-to-python.png?branch=master
   :target: https://travis-ci.org/sixty-north/introduction-to-python
