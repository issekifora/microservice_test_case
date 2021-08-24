import os

import pika

rabbit_user = os.getenv("RABBIT_USER")
rabbit_pass = os.getenv("RABBIT_PASS")
rabbit_host = os.getenv("RABBIT_HOST")
rabbit_port = os.getenv("RABBIT_PORT")
queue = os.getenv("QUEUE", "queue")

credentials = pika.PlainCredentials(rabbit_user, rabbit_pass)

import logging.config

logging.config.fileConfig(fname="logging.ini")
