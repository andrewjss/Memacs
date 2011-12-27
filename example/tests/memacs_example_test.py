# -*- coding: utf-8 -*-
# Time-stamp: <2011-10-28 15:13:31 aw>

import unittest
import sys
import os
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)))))
from example.memacs_example import Foo


class TestFoo(unittest.TestCase):

    def setUp(self):
        pass

    def test_all(self):
        argv = "-s"
        memacs = Foo(argv=argv.split())
        # or when in append mode:
        # memacs = Foo(argv=argv.split(), append=True)
        data = memacs.test_get_entries()

        # generate assertEquals :)
        #for d in range(len(data)):
        #    print "self.assertEqual(data[%d], \"%s\")" % \
        #        (d, data[d])

        self.assertEqual(data[0], "** foo")
        self.assertEqual(data[1], "   :PROPERTIES:")
        #self.assertEqual(data[2], "  :CREATED: <2011-12-20 Tue 16:55:50>")
        #changes every time (due to created sets localtime )
        #self.assertEqual(data[3],
        # "   :ID:      608b1af4f65f98b67c7dfa6a470b319d456e5504")
        self.assertEqual(data[4], "   :END:")
        self.assertEqual(data[5], "** bar\t:tag1:tag2:")
        self.assertEqual(data[6], "   bar notes")
        self.assertEqual(data[7], "   foo notes")
        self.assertEqual(data[8], "   :PROPERTIES:")
        self.assertEqual(data[9], "   :DESCRIPTION: foooo")
        self.assertEqual(data[10], "   :CREATED:     <1970-01-01 Thu 00:00>")
        #changes every time (due to created sets localtime )
        #self.assertEqual(data[3],
        #"   :ID:      608b1af4f65f98b67c7dfa6a470b319d456e5504")
        self.assertEqual(data[12], "   :END:")

    def tearDown(self):
        pass
