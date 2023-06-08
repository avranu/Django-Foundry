"""

	Metadata:

		File: thefuzz.py
		Project: Django Foundry
		Created Date: 26 Mar 2023
		Author: Jess Mann
		Email: jess.a.mann@gmail.com

		-----

		Last Modified: Wed May 10 2023
		Modified By: Jess Mann

		-----

		Copyright (c) 2023 Jess Mann
"""

from __future__ import annotations
from typing import Iterable
from thefuzz import fuzz, process
from matching.engine import MatchingEngine

class TheFuzz(MatchingEngine):

	def choose( self, input : str, choices : Iterable[str], required_confidence : int = 90 ) -> tuple[str, int]:
		"""
		Use the matching engine to pick the best option from a group of options

		Args:
			input (str):
				The input to attempt to match
			choices (Iterable[str]):
				A group of choices to pick between
			required_confidence (int, optional):
				The lowest confidence to "accept". If no match is found with this confidence, we will return None.
				Defaults to 90.

		Returns:
			tuple[str | None, int]:
			(match, confidence)

			Match: The matching choice, or None
			Confidence: The confidence of the match, from 1-100
		"""
		(matching_key, confidence) = process.extractOne(str(input), choices)

		# Not a sufficient match.
		if confidence < required_confidence:
			return (None, 100 - confidence)

		# Sufficient match!
		return (matching_key, confidence)

	def match( self, input : str, compare : str ) -> int:
		"""
		Use the matching engine to determine the confidence that these two strings match.

		For example:
			"John Smith" == "John Smith"
			"John Edward Smith" != "John Smith"
			"Smith, John" != "John Smith"

		Args:
			input (str):
				The input to attempt to match

		Returns:
			int:
				The confidence that these two strings match.
			 	1 - 100

				100 means we are certain they match.
				1 means we are certain they do not match.
		"""
		return fuzz.ratio(input, compare)

	def partial_match( self, input : str, compare : str ) -> int:
		"""
		Use the matching engine to determine the confidence that these two strings have a partial match.

		For example:
			"John Edward Smith" == "John Smith"

		Args:
			input (str):
				The input to attempt to match

		Returns:
			int:
				The confidence that these two strings match.
			 	1 - 100

				100 means we are certain they match.
				1 means we are certain they do not match.
		"""
		return fuzz.partial_ratio(input, compare)

	def token_match( self, input : str, compare : str ) -> int:
		"""
		Use the matching engine to determine the confidence that each token (i.e. string part) of these two strings match.

		For example:
			"Smith, John" == "John Smith"

		Args:
			input (str):
				The input to attempt to match

		Returns:
			int:
				The confidence that these two strings match.
			 	1 - 100

				100 means we are certain they match.
				1 means we are certain they do not match.
		"""
		return fuzz.token_sort_ratio(input, compare)

	def token_partial_match( self, input : str, compare : str ) -> int:
		"""
		Use the matching engine to determine the confidence that these two strings match.

		For example:
			"Smith, John Edward" == "John Smith"

		Args:
			input (str):
				The input to attempt to match

		Returns:
			int:
				The confidence that these two strings match.
			 	1 - 100

				100 means we are certain they match.
				1 means we are certain they do not match.
		"""
		return fuzz.token_set_ratio(input, compare)
