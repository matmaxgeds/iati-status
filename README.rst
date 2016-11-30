IATI Website Tests
==================

.. image:: https://travis-ci.org/IATI/IATI-Website-Tests.svg?branch=master
    :target: https://travis-ci.org/IATI/IATI-Websites-Tests
.. image:: https://requires.io/github/IATI/IATI-Website-Tests/requirements.svg?branch=master
    :target: https://requires.io/github/IATI/IATI-Website-Tests/requirements/?branch=master
    :alt: Requirements Status
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/IATI/IATI-Website-Tests/blob/master/LICENSE


Introduction
------------

This repository contains smoke tests and sanity checks for all live IATI websites.

The output of tests can be been at: https://travis-ci.org/IATI/IATI-Website-Tests


Technology Overview
-------------------

Tests are written using `pytest <http://doc.pytest.org>`_.

These tests are run daily (at around 12noon) using Travis `cron jobs <https://docs.travis-ci.com/user/cron-jobs/>`_.



Installation
------------

.. code-block:: bash

	# Download dependencies
	sudo apt-get install virtualenv

	# Create a virtual environment using python 3
	virtualenv -p python3 pyenv

	# Activate the virtual environment
	source pyenv/bin/activate

	# Install requirements
	pip install -r requirements.txt

	# Run the tests
	py.test tests/
