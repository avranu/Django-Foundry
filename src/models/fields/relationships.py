"""


	Metadata:

		File: relationships.py
		Project: Django Foundry
		Created Date: 18 Aug 2022
		Author: Jess Mann
		Email: jess.a.mann@gmail.com

		-----

		Last Modified: Sat Dec 03 2022
		Modified By: Jess Mann

		-----

		Copyright (c) 2022 Jess Mann

"""
# Generic imports
from __future__ import annotations

# Django Imports
import auto_prefetch
# Lib Imports
# App Imports

class ForeignKey(auto_prefetch.ForeignKey):
    pass


class OneToOneField(auto_prefetch.OneToOneField):
    pass

