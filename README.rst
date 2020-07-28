IATI Service Monitor
====================

This repository contains smoke tests and sanity checks for some live IATI websites and web tools.

The current status of the tests can be seen on the badge below:

.. image:: https://travis-ci.com/codeforIATI/iati-service-monitor.svg?branch=main
    :target: https://travis-ci.com/codeforIATI/iati-service-monitor

Tests are run daily using Travis `cron jobs <https://docs.travis-ci.com/user/cron-jobs/>`_.

Setup
-----

.. code-block:: bash

	# Create a virtual environment using python 3
	python3 -m venv venv

	# Activate the virtual environment
	source venv/bin/activate

	# Install requirements
	pip install -r requirements.txt

	# Run the tests
	pytest
