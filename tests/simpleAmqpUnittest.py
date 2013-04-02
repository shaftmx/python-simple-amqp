#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import sys
import pika
import logging
import mock

#myPath = os.path.abspath(os.path.dirname(__file__))
#sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/../src'))

from simpleamqp import SimpleAmqp

class SimpleAmqpTestCase(unittest.TestCase):

    def get_init(self):
        self._q = SimpleAmqp(pool=['rabbit1', 'rabbit2'], pooltype='L')
        logging.getLogger('simpleAmqp').setLevel(logging.CRITICAL)
        self._q._connect = mock.Mock()

    def setUp(self):
        self.get_init()

    def tearDown(self):
        pass

    def test_send(self):
        self._q.send('foo','bar')
        self.assertTrue(True)
