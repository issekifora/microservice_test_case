import pytest

from microservice_template.src.reverse_string import reverse_string
from microservice_template.src.utils import prepare_response_success, prepare_request, prepare_response_error
from schema import validator_request, validator_response


@pytest.mark.unit
def test_reverse_string(string):
    reversed = reverse_string(string)
    assert reversed == "арозА упал ан алапу азор А"


@pytest.mark.unit
def test_prepare_request(string):
    request = prepare_request(string)
    validator_request(request)


@pytest.mark.unit
def test_prepare_response_success(string):
    response = prepare_response_success(string)
    validator_response(response)


@pytest.mark.unit
def test_prepare_response_error():
    response = prepare_response_error(code=-1, message="Error")
    validator_response(response)
