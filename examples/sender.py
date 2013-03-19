#!/usr/bin/env python
import pika
import random
import logging

from simpleamqp import SimpleAmqp

# Init logging level
logging.getLogger('simpleAmqp').setLevel(logging.CRITICAL)

# Add handler for debug
logging.getLogger('simpleAmqp').setLevel(logging.INFO)
logging.getLogger('simpleAmqp').addHandler(logging.StreamHandler())

q = SimpleAmqp(pool=['rabbit1', 'rabbit2'], pooltype='L')
try:
    q.send('hello',"My message")
except:
    logging.critical("Send message error")

try:
    messages = ["Many message","Many message2"]
    q.sendMany('hello',messages)
except:
    logging.critical("Send message error")
