IATI Service Monitor
====================

This repository contains smoke tests and sanity checks for some live IATI websites and web tools.

The current status of the tests can be seen on the badge below:

.. image:: https://raw.githubusercontent.com/codeforIATI/iati-service-monitor/gh-pages/status.svg
    :target: https://status.codeforiati.org/

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
