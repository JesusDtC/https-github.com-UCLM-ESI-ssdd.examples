#!/usr/bin/env python3
# Extracted from: https://www.rabbitmq.com/tutorials/tutorial-two-python.html

import sys
import pika


def send_message(message):
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2  # make message persistent
        ))

    print("[x] Sent: ", message)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

for msg in sys.argv[1:]:
    send_message(msg)

connection.close()
