#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import sys
import pika
import logging

#myPath = os.path.abspath(os.path.dirname(__file__))
#sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/../src'))

from simpleamqp import SimpleAmqp

#class FakeRabbitChannel(pika.channel):
class FakeRabbitChannel(object):
    def __init__(self):
        return
    def queue_declare(self,queue):
        return
    def basic_publish(self,**params):
        return

class FakeRabbitConnect(pika.BlockingConnection):
    def __init__(self,pika_param):
        return

    def channel(self):
        return FakeRabbitChannel()

    def __call__(self):
        return self


def fakeConnect():
    return FakeRabbitConnect(pika.ConnectionParameters('rabbit1'))

class SimpleAmqpTestCase(unittest.TestCase):

    def get_init(self):
        self._q = SimpleAmqp(pool=['rabbit1', 'rabbit2'], pooltype='L')
        logging.getLogger('simpleAmqp').setLevel(logging.CRITICAL)
        self._q._connect = fakeConnect()

    def setUp(self):
        self.get_init()

    def tearDown(self):
        pass

    def test_send(self):
        self._q.send('foo','bar')
        self.assertTrue(True)
