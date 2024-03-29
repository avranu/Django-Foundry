"""
	Custom argparse Action.

	Modified from https://stackoverflow.com/questions/43968006/support-for-enum-arguments-in-argparse

	Metadata:

		File: action.py
		Project: Django Foundry
		Created Date: 06 Sep 2022
		Author: Alexander Lanin, Tim, Jess Mann
		Email: jess.a.mann@gmail.com

		-----

		Last Modified: Sat Dec 03 2022
		Modified By: Jess Mann

		-----

		Copyright (c) 2022 Jess Mann
"""
import argparse
import enum
from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)

class EnumAction(argparse.Action):
	"""
	Argparse action for handling Enums
	"""

	def __init__(self, **kwargs):
		# Pop off the type value
		enum_type = kwargs.pop("type", None)

		# Ensure an Enum subclass is provided
		if enum_type is None:
			raise ValueError("type must be assigned an Enum when using EnumAction")
		if not issubclass(enum_type, enum.Enum):
			raise TypeError("type must be an Enum when using EnumAction")

		# Generate choices from the Enum
		try:
			kwargs.setdefault("choices", tuple(e.value.lower() for e in enum_type))
		except Exception as e:
			logger.critical(f'Exception setting enum choices for argparse. This can happen if the enum is set with a non-string value. "{e}"')
			raise e

		super().__init__(**kwargs)

		self._enum = enum_type

	def __call__(self,
				 parser: argparse.ArgumentParser,
				 namespace: argparse.Namespace,
				 value: Any,
				 option_string: Optional[str] = None):

		# Convert value back into an Enum
		if isinstance(value, str):
			value = self._enum[value.upper()]
			setattr(namespace, self.dest, value)
		elif value is None:
			raise argparse.ArgumentTypeError(f"You need to pass a value after {option_string}!")
		else:
			# A pretty invalid choice message will be generated by argparse
			raise argparse.ArgumentTypeError()