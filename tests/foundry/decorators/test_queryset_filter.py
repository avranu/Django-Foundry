import pytest
from unittest.mock import patch, MagicMock
from djangofoundry.decorators.queryset_filter import Queryset_Filter

class TestQuerysetFilter:

    def test_init(self):
        def filter_fn():
            return "filter result"
        queryset_filter = Queryset_Filter(filter_fn, "test_filter")
        assert queryset_filter.filter_fn == filter_fn
        assert queryset_filter.name == "test_filter"

    def test_set_name(self):
        def filter_fn():
            return "filter result"
        queryset_filter = Queryset_Filter(filter_fn, "test_filter")
        queryset_filter.__set_name__(MagicMock(filters={}), "test_filter")
        assert "test_filter" in queryset_filter.queryset.filters

    def test_get(self):
        def filter_fn():
            return "filter result"
        queryset_filter = Queryset_Filter(filter_fn, "test_filter")
        queryset_filter.__get__(None, MagicMock())
        assert queryset_filter.queryset is None

    def test_call(self):
        def filter_fn(*args, **kwargs):
            return "filter result"
        queryset_filter = Queryset_Filter(filter_fn, "test_filter")
        result = queryset_filter(1, 2, 3, test="test")
        assert result == "filter result"
