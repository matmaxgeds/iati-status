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

This repository contains tests of the live websites.

Currently only the dashboard is tested.

These tests are run daily by Travis `cron jobs <http://example.com>`_: https://travis-ci.org/IATI/IATI-Website-Tests

Since travis is not designed for daily tests (rather for per commit tests) this causes some odd behaviour.


Installation
------------

.. code-block:: bash

	# Download dependencies
	sudo apt-get install virtualenv

	# Create a virtual environment
	virtualenv pyenv

	# Activate the virtual environment
	source pyenv/bin/activate

	# Install requirements
	pip install -r requirements.txt

	# Run the tests
	py.test tests/
