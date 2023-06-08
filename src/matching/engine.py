"""
	
	Metadata:
	
		File: engine.py
		Project: Django Foundry
		Created Date: 27 Dec 2022
		Author: Jess Mann
		Email: jess.a.mann@gmail.com
	
		-----
	
		Last Modified: Mon May 01 2023
		Modified By: Jess Mann
	
		-----
	
		Copyright (c) 2022 Jess Mann
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable


class MatchingEngine(ABC):

	@abstractmethod
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

	@abstractmethod
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

	@abstractmethod
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

	@abstractmethod
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

	@abstractmethod
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