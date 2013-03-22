# -*- coding: utf-8 -*-

import unittest
from simpleAmqpUnittest import SimpleAmqpTestCase

def all_tests():
    suite = unittest.TestSuite()
    # Redis
    suite.addTest(unittest.makeSuite(SimpleAmqpTestCase))
    return suite

#self.assertRaises(TypeError, adder, 33, 'a string')

