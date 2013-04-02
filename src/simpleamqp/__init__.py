#!/usr/bin/env python
import pika
import random
import logging

class SimpleAmqp:

    def __init__(self, pool, pooltype='F'):
        # Disable pika log
        logging.getLogger('pika').setLevel(logging.CRITICAL)
        self._logger = logging.getLogger('simpleAmqp')
        self._pool = pool
        self._pooltype = pooltype # L : load Balancing / F fail over
        self._debugmsg = ''

    def _connect(self):
        if self._pooltype == 'L': # LB
            poollist = list(self._pool) # make a copy
            random.shuffle(poollist)
        else:
            poollist = self._pool
        for ip in poollist:
            self._debugmsg = ip
            try:
                self._logger.info("Try connect to node %s" % ip)
                return pika.BlockingConnection(pika.ConnectionParameters(ip))
            except:
                self._logger.warning("Connection node %s failed" % ip)
                continue
        self._logger.error("Node connection AllNodesFailed")
        raise Exception("AllNodesFailed")

    def _close(self,connect):
        return connect.close()

    def send(self, queue, message):
        c = self._connect()
        channel = c.channel()
        # Create queue
        channel.queue_declare(queue=queue)
        # send message on queue
        channel.basic_publish(exchange='',
                                routing_key=queue,
                                body=message+' '+self._debugmsg)
        self._close(c)

    def _callback(self, ch, method, properties, body):
        self._logger.info("[x] Received %r" % body)

    def recv(self, queue, callback=None):
        if callback is None:
            callback = self._callback
        c = self._connect()
        channel = c.channel()
        # Create queue
        channel.queue_declare(queue=queue)
        self._logger.info("[*] Waiting for messages. To exit press CTRL+C")
        channel.basic_consume(callback,
                              queue=queue,
                              no_ack=True)
        channel.start_consuming()

    def sendMany(self, queue, messages):
        c = self._connect()
        for message in messages:
            channel = c.channel()
            # Create queue
            channel.queue_declare(queue=queue)
            # send message on queue
            channel.basic_publish(exchange='',
                                    routing_key=queue,
                                    body=message+' '+self._debugmsg)
        self._close(c)

