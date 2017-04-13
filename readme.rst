.. class:: no-web no-pdf

|travis| |heroku|


Superlists
=========

Simple Django to-do app.


Installation
---------

Follow the below steps to set it up on a machine. Preferably manage python packages using virtual environments like virtualenvwrapper_ , virtualenv_ or venv_ which comes with ``python >= 3.3``

.. code::

  git clone https://github.com/sfarzy/superlists.git
  cd superlists
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py collectstatic --noinput
  python manage.py runserver


Testing
-------

To run the unit tests.

::

  python manage.py test lists, accounts
  
To run the functional test you should have the latest geckodriver_ for firefox installed. 

::

  python manage.py test functional_tests
  
  
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
.. _virtualenv: https://pypi.python.org/pypi/virtualenv
.. _venv: https://docs.python.org/3/library/venv.html
.. _geckodriver: https://github.com/mozilla/geckodriver/releases/latest

.. |travis| image:: https://travis-ci.org/sfarzy/superlists.svg?branch=master
    :target: https://travis-ci.org/sfarzy/superlists
    :alt: travis

.. |heroku| image:: https://img.shields.io/badge/heroku-deployed-blue.svg
      :target: https://sfarzy-superlists.herokuapp.com
      :alt: Heroku
