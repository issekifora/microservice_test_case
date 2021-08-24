import os
import time

import pika
import pika.exceptions
import pytest

from config import credentials


@pytest.fixture
def string():
    string = "А роза упала на лапу Азора"
    return string


@pytest.fixture
def reversed_string():
    string = "арозА упал ан алапу азор А"
    return string


@pytest.mark.functional
@pytest.mark.usefixtures("client_class")
@pytest.fixture(scope="session")
def test_client():
    from microservice_template.app import application as flask_app

    flask_app.debug = True
    flask_app.config["TESTING"] = True
    flask_app.config["SERVER_NAME"] = "localhost"
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture
def api_spec():
    from prance import ResolvingParser

    parser = ResolvingParser("microservice_template/app/specs/api.yaml", backend="openapi-spec-validator", strict=False)

    return parser.specification


@pytest.fixture
def queue():
    return "queue"


@pytest.fixture
def queue_errors():
    return "queue_errors"


@pytest.fixture(scope="session")
def rabbit_connection():

    rabbit_host = "0.0.0.0"
    rabbit_port = os.getenv("RABBITMQ_5672_TCP")
    connected = False
    while not connected:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=rabbit_host,
                    port=rabbit_port,
                    heartbeat=120,
                    credentials=credentials,
                    blocked_connection_timeout=180,
                )
            )

            yield connection
            connected = True
            connection.close()
        except pika.exceptions.IncompatibleProtocolError:
            # wait until RabbitMQ becomes available
            time.sleep(1)
            connected = False
