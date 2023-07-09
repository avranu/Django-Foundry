import pytest
from unittest.mock import patch, MagicMock
from time import sleep
from djangofoundry.decorators.retry import retry

class TestRetry:

    def test_retry_success(self):
        # Function that always succeeds
        @retry(tries=5, delay=1, backoff=2)
        def test_func():
            return True
        assert test_func() == True

    def test_retry_failure(self):
        # Function that always fails
        @retry(tries=5, delay=1, backoff=2)
        def test_func():
            return False
        assert test_func() == False

    @patch('time.sleep', side_effect=InterruptedError)
    def test_retry_interrupted(self, mock_sleep):
        # Function that is interrupted
        @retry(tries=5, delay=1, backoff=2)
        def test_func():
            return False
        with pytest.raises(InterruptedError):
            test_func()

    def test_retry_invalid(self):
        with pytest.raises(ValueError):
            @retry(tries=-1, delay=1, backoff=2)
            def test_func():
                return True

        with pytest.raises(ValueError):
            @retry(tries=5, delay=0, backoff=2)
            def test_func():
                return True

        with pytest.raises(ValueError):
            @retry(tries=5, delay=1, backoff=1)
            def test_func():
                return True
