import pytest

from microservice_test_case.src.is_palindrome import is_palindrome


@pytest.mark.unit
def test_reverse_string(string):
    assert is_palindrome(string) is True
