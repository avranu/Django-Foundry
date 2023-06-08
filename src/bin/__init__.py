"""
	This directory contains scripts that can be run from the commandline to interact with our application and its associated tools.

	These files should not be imported into django.

	Find out about each of these tools and their options by running them with the --help option.

	Examples:
		>>> python db.py --help

	Metadata:

		File: __init__.py
		Project: Django Foundry
		Created Date: 06 Sep 2022
		Author: Jess Mann
		Email: jess.a.mann@gmail.com

		-----

		Last Modified: Sat Dec 03 2022
		Modified By: Jess Mann

		-----

		Copyright (c) 2022 Jess Mann
"""
# Do not import anything here, because we don't want these files imported elsewhere.
from .utils import *