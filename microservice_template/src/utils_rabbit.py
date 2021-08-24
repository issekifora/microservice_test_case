def declare_queue(channel, queue, durable, **kwargs):
    channel.exchange_declare(exchange=queue, exchange_type="direct")
    channel.queue_declare(queue=queue, durable=durable, **kwargs)
    channel.queue_bind(exchange=queue, queue=queue, routing_key="")
