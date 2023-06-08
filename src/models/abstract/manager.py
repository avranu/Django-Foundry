"""

	Metadata:

		File: manager.py
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

from typing_extensions import Self
from typing import Callable, Any, Iterable, Optional
# Django Imports
# Django extensions
import auto_prefetch
from psqlextra.manager import PostgresManager as PGManager
# Lib Imports
# App Imports

class Universe:
	"""
	A mixin that all managers inherit from that provides filtering for our "universe" of data.
	"""
	def universe(self) -> Self:
		"""
		Retrieves all data matching our default criteria.

		Subclasses should override this method.

		Similar to all(), but does basic filtering that is consistent across our app.

		As of 2022-09-01, this should retrieve all data associated with open recalc cases. It should not be assumed that this will always use that criteria.

		Returns:
			QuerySet: A QuerySet filtered by the default criteria
		"""
		raise NotImplementedError()

class Manager(Universe, auto_prefetch.Manager):
	'''
	A custom query manager. This creates QuerySets and is used in all models interacting with the db.
	'''


class PostgresManager(Universe, PGManager):
	'''
	A custom query manager. This creates querysets and is used in all models interacting with the db (when that db is postgres)
	'''
