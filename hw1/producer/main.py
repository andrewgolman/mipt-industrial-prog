#!/usr/bin/env python

import pika
import random
import time
import os


def main():
    print(f" [x] Start producer'", flush=True)
    retry_time = 1
    while True:
        try:
            connection = pika.BlockingConnection(pika.URLParameters(os.getenv("RabbitURL")))
            channel = connection.channel()
            channel.queue_declare(queue='hw1')
            while True:
                value = random.randint(-2 ** 32, 2 ** 32 - 1)
                channel.basic_publish(exchange='',
                                      routing_key='hw1',
                                      body=str(value))
                print(f" [x] Sent '{value}'", flush=True)
                time.sleep(1)
                retry_time = 1

        except pika.exceptions.ConnectionClosed:
            print(f" [x] Connection refused, retry in {retry_time} sec'", flush=True)
            time.sleep(retry_time)
            retry_time *= 2


if __name__ == "__main__":
    main()
