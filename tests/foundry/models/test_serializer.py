import pytest
from unittest.mock import patch, MagicMock
from rest_framework import serializers
from djangofoundry.models.serializer import Serializer

# A concrete serializer for testing the abstract Serializer
class TestSerializer(Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        fields = ['id', 'name']
        generated_fields = ['name']

class TestSerializerClass:

    @pytest.fixture
    def test_serializer(self):
        return TestSerializer(data={"id": 1, "name": "Test"})

    def test_init_exclude_fields(self, test_serializer):
        test_serializer.context = {'exclude_fields': ['id']}
        test_serializer.__init__()
        assert 'id' not in test_serializer.fields

    def test_init_include_fields(self, test_serializer):
        test_serializer.context = {'include_fields': ['id']}
        test_serializer.__init__()
        assert 'name' not in test_serializer.fields

    def test_get_fieldnames(self, test_serializer):
        assert TestSerializer.get_fieldnames() == ['id', 'name']

    def test_get_native_fields(self, test_serializer):
        assert TestSerializer.get_native_fields() == ['id']
