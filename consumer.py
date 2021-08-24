import logging.config

import pika

from config import rabbit_host, rabbit_port, queue, credentials
from microservice_template.src.reverse_string_consume import reverse_string_consume
from microservice_template.src.utils_rabbit import declare_queue

logging.config.fileConfig(fname="logging.ini", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=rabbit_host, port=rabbit_port, heartbeat=100, credentials=credentials, blocked_connection_timeout=100
    )
)
channel = connection.channel()


declare_queue(channel, queue, durable=True, arguments={"x-max-length": 1000, "x-overflow": "reject-publish"})

channel.confirm_delivery()

logging.info("Starting to consume messages")
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue, on_message_callback=reverse_string_consume)
channel.start_consuming()
channel.close()
