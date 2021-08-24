import json

import pika
import pytest

from microservice_template.src.reverse_string_consume import reverse_string_consume
from microservice_template.src.utils import prepare_request
from microservice_template.src.utils_rabbit import declare_queue
from schema import validator_response


@pytest.mark.integration
def test_declare_queue(rabbit_connection):
    assert rabbit_connection.is_open


@pytest.mark.integration
def test_rabbit_declare(rabbit_connection, queue, string):
    channel = rabbit_connection.channel()

    declare_queue(channel, queue, durable=True)

    request = prepare_request(string=string)

    channel.basic_publish(
        exchange="", routing_key=queue, body=json.dumps(request), properties=pika.BasicProperties(delivery_mode=2,),
    )

    assert channel.is_open


@pytest.mark.integration
def test_reverse_string_consume(rabbit_connection, queue, reversed_string):
    channel = rabbit_connection.channel()

    channel.queue_declare(queue=queue, durable=True)

    channel.confirm_delivery()

    method_frame, header_frame, body = channel.basic_get(queue=queue)

    result = reverse_string_consume(channel, method_frame, body)
    assert validator_response(result)
    assert result["result"]["string"] == reversed_string


@pytest.mark.integration
def test_reverse_string_consume_ack(rabbit_connection, queue):
    channel = rabbit_connection.channel()

    channel.queue_declare(queue=queue, durable=True)

    channel.confirm_delivery()

    method_frame, header_frame, body = channel.basic_get(queue=queue)

    assert method_frame is None


@pytest.mark.integration
def test_corrupted_message_send(rabbit_connection, queue_errors):
    channel = rabbit_connection.channel()

    declare_queue(channel, queue_errors, durable=True)

    request = prepare_request(string=None)

    channel.basic_publish(
        exchange="",
        routing_key=queue_errors,
        body=json.dumps(request),
        properties=pika.BasicProperties(delivery_mode=2,),
    )

    channel.basic_publish(
        exchange="", routing_key=queue_errors, body="", properties=pika.BasicProperties(delivery_mode=2,),
    )

    assert channel.is_open


@pytest.mark.integration
def test_corrupted_message_receive(rabbit_connection, queue_errors):
    channel = rabbit_connection.channel()

    channel.queue_declare(queue=queue_errors, durable=True)

    channel.confirm_delivery()

    while True:

        method_frame, header_frame, body = channel.basic_get(queue=queue_errors)
        if method_frame is None:
            break

        result = reverse_string_consume(channel, method_frame, body)
        assert validator_response(result)
        assert "error" in result
