import json
import logging.config

import fastjsonschema

from microservice_template.src.reverse_string import reverse_string
from microservice_template.src.utils import prepare_response_success, prepare_response_error
from schema import validator_request

logger = logging.getLogger(__name__)

def reverse_string_consume(channel, method, body):
    body_decoded = body.decode("utf-8")

    try:
        message = json.loads(body_decoded)
    except json.decoder.JSONDecodeError as error:
        logger.error(str(error), exc_info=True)
        error = prepare_response_error(code=-1, message=str(error), _id=None)
        channel.basic_ack(delivery_tag=method.delivery_tag)
        return error

    try:
        validator_request(message)
        string_ = message["params"]["string"]

        _id = message.get("id", None)

        reversed_string = reverse_string(string_)
        result = prepare_response_success(reversed_string, _id)
        channel.basic_ack(delivery_tag=method.delivery_tag)
        return result

    except fastjsonschema.exceptions.JsonSchemaException as error:
        _id = message.get("id", None)
        _error = str(error)
        logger.error(_error, exc_info=True)
        error = prepare_response_error(code=1000, message=_error, _id=_id)
        channel.basic_ack(delivery_tag=method.delivery_tag)
        return error
