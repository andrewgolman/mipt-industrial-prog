#!/usr/bin/env python

import pika
import time
import os


def callback(ch, method, properties, body):
    print(f" [*] Received {body}", flush=True)


def main():
    print(f" [*] Start consumer'", flush=True)
    retry_time = 1
    while True:
        try:
            connection = pika.BlockingConnection(pika.URLParameters(os.getenv("RabbitURL")))
            channel = connection.channel()
            channel.queue_declare(queue='hw1')

            channel.basic_consume(callback, queue='hw1', no_ack=True)
            retry_time = 1
            channel.start_consuming()

        except pika.exceptions.ConnectionClosed:
            print(f" [*] Connection refused, retry in {retry_time} sec'", flush=True)
            time.sleep(retry_time)
            retry_time *= 2


if __name__ == "__main__":
    main()
