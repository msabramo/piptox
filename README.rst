piptox
======

Sample usage::

    piptox git+https://github.com/zbyte64/django-dockit.git

This downloads from the above URL into a temporary directory using
`pip <http://www.pip-installer.org/>`_ and then runs
`tox <http://tox.testrun.org/>`_ in that directory. This gives you a very quick
and dirty poor man's CI system.

For more info::

    piptox --help
