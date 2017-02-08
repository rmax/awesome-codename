================
Awesome Codename
================

.. image:: https://img.shields.io/pypi/v/awesome-codename.svg
        :target: https://pypi.python.org/pypi/awesome-codename

.. image:: https://img.shields.io/pypi/pyversions/awesome-codename.svg
        :target: https://pypi.python.org/pypi/awesome-codename

.. image:: https://readthedocs.org/projects/awesome-codename/badge/?version=latest
        :target: https://readthedocs.org/projects/awesome-codename/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/travis/rolando/awesome-codename.svg
        :target: https://travis-ci.org/rolando/awesome-codename

.. image:: https://codecov.io/github/rolando/awesome-codename/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/rolando/awesome-codename

.. image:: https://landscape.io/github/rolando/awesome-codename/master/landscape.svg?style=flat
    :target: https://landscape.io/github/rolando/awesome-codename/master
    :alt: Code Quality Status

.. image:: https://requires.io/github/rolando/awesome-codename/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/rolando/awesome-codename/requirements/?branch=master

Awesome Codename Generator

* Free software: AGPL v3 license
* Documentation: https://awesome-codename.readthedocs.org.
* Python versions: 2.7, 3.4+

Features
--------

Generates awesome codenames :)


Quickstart
----------

You can use the ``generate_codename()`` function and pick your favorite::

  >>> from awesome_codename import generate_codename
  >>> generate_codename()
  'abnormal keeper'
  >>> generate_codename()
  'altruistic supermodel'
  >>> generate_codename()
  'recovered image'

Or run ``awesome-codename`` from the command line::

  $ awesome-codename 3
  square thermometer
  best shaker
  countywide fusion


Credits
-------

All credits go to `SecureDrop`_ project for curating the list of adjectives and nouns.

This package was created with Cookiecutter_ and the `rolando/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`rolando/cookiecutter-pypackage`: https://github.com/rolando/cookiecutter-pypackage
.. _SecureDrop: https://securedrop.org/
