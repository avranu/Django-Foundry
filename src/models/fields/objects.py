"""


	Metadata:

		File: objects.py
		Project: Django Foundry
		Created Date: 22 Aug 2022
		Author: Jess Mann
		Email: jess.a.mann@gmail.com

		-----

		Last Modified: Thu May 04 2023
		Modified By: Jess Mann

		-----

		Copyright (c) 2022 Jess Mann

"""
# Generic imports
from __future__ import annotations
from typing import Any
# 3rd party packages
import orjson
# Django imports
from django.db.models import JSONField, Func, FloatField
from django.core import exceptions
# 3rd Party imports
from psqlextra import fields
import picklefield.fields

class HStoreField(fields.HStoreField):
	pass

class JSONField(JSONField):
	'''
    def get_prep_value(self, value):
        if value is None:
            return value
        return orjson.dumps(value)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        try:
            orjson.dumps(value)
        except TypeError:
            raise exceptions.ValidationError(
                self.error_messages["invalid"],
                code="invalid",
                params={"value": value},
            )
	'''

class JsonFloatValues(Func):
    function = 'jsonb_each_text'

    def __init__(self, expression, **extra):
        super().__init__(expression, output_field=FloatField(), **extra)

class PickledObjectField(picklefield.fields.PickledObjectField):
	pass