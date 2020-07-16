IATI Service Monitor
====================

This repository contains smoke tests and sanity checks for some live IATI websites and web tools.

The current status of the tests can be seen on the badge below:

.. image:: https://travis-ci.com/codeforIATI/iati-service-monitor.svg?branch=master
    :target: https://travis-ci.com/codeforIATI/iati-service-monitor

Tests are run daily using Travis `cron jobs <https://docs.travis-ci.com/user/cron-jobs/>`_.

Setup
-----

.. code-block:: bash

	# Create a virtual environment using python 3
	python3 -m venv pyenv

	# Activate the virtual environment
	source pyenv/bin/activate

	# Install requirements
	pip install -r requirements.txt

	# Login credentials for the IATI backup server are stored as environment variables.
	# Add these lines to the end of your virtualenv set-up script - i.e. pyenv/bin/activate
	export backup_server_hostname='[YOUR_HOSTNAME]'
	export backup_server_username='[YOUR_USERNAME]'
	export backup_server_password='[YOUR_PASSWORD]'

	# Run the tests
	py.test tests/
