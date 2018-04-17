#!/usr/bin/env python3

import os
import sys
# Stick that in at the front so that it takes precedence over an installed version.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../src/python/")))

def assert_floats_equal(expected, actual, margin=0.0001, name=None):
    difference = abs(actual/expected - 1)
    message = "Expected: {}\nActual: {}\nMargin: {}\nDifference: {}".format(expected, actual, margin, difference)
    if name:
        print(name)
    print(message)
    if difference > margin:
        print("FAILURE\n")
        return False
    else:
        print("success\n")
        return True
