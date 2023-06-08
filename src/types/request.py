"""

	Metadata:

	    File: types.py
		Project: Django Foundry
	    Created Date: 13 Oct 2022
	    Author: Jess Mann
	    Email: jess.a.mann@gmail.com

	    -----

		Last Modified: Sat Dec 03 2022
		Modified By: Jess Mann

	    -----

	    Copyright (c) 2022 Jess Mann
"""
from enum import Enum

class RequestType(Enum):
    """
    Valid types of HTTP Requests
    """
    GET = 'GET'
    POST = 'POST'