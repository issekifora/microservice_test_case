import logging.config
import os


credentials = pika.PlainCredentials(rabbit_user, rabbit_pass)

logging.config.fileConfig(fname="logging.ini")
