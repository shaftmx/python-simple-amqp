#!/usr/bin/env python
import pika
import logging

from simpleamqp import SimpleAmqp

def mycallback(ch, method, properties, body):
    print "mycallback %s" % body

# Init logging level
logging.getLogger('simpleAmqp').setLevel(logging.CRITICAL)

# Add handler for debug
logging.getLogger('simpleAmqp').setLevel(logging.INFO)
logging.getLogger('simpleAmqp').addHandler(logging.StreamHandler())

q = SimpleAmqp(pool=['rabbit1', 'rabbit2'], pooltype='F')
q._callback = mycallback
try:
    q.recv('hello')
except:
    logging.critical("Recv message error")
