#!/usr/bin/env python3

import json
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

def assert_dicts_equal(expected, actual, name=None):
    if name:
        print(name)
    expected_blob = json.dumps(expected, indent=2, sort_keys=True)
    actual_blob = json.dumps(actual, indent=2, sort_keys=True)
    if expected_blob == actual_blob:
        print("success")
        return True
    else:
        print("FAILURE\nExpected:\n{}\nActual:\n{}".format(expected_blob, actual_blob))
        return False

def data_path(fname):
    return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", fname))
