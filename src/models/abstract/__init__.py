"""
	Model classes that must be implemented by our applications.

	Metadata:

		File: __init__.py
		Project: Django Foundry
		Created Date: 22 Aug 2022
		Author: Jess Mann
		Email: jess.a.mann@gmail.com

		-----

		Last Modified: Sat Dec 03 2022
		Modified By: Jess Mann

		-----

		Copyright (c) 2022 Jess Mann

"""
# Generic imports
from .queryset import *
from .manager import Manager, PostgresManager
from .model import Model