piptox
======

.. image:: https://secure.travis-ci.org/msabramo/piptox.png?branch=master
   :target: http://travis-ci.org/msabramo/piptox

Sample usage::

    piptox git+https://github.com/msabramo/piptox.git    # Yes, you can run piptox on its own repo :-)

This downloads from the above URL into a temporary directory using
`pip <http://www.pip-installer.org/>`_ and then runs
`tox <http://tox.testrun.org/>`_ in that directory. This gives you a very quick
and dirty poor man's CI system.

For more info::

    piptox --help
