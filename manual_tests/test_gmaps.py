#!/usr/bin/env python3

from _test_base import *
import argparse
import agf.gmaps

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key", required=True,
                    help="Google Maps developer API key.")
    return vars(parser.parse_args())

def test_bearing_haversine(*args, **kwargs):
    cases = [
        {
            "start":(37.538592, -77.433766),
            "end":(37.555782, -77.456293),
            "bearing":313.90397878289707,
            "haversine":2.756414517586141
        },
        {
            "start":(6.275069, -6.882270),
            "end":(-5.243421, 15.482296),
            "bearing":117.29027556210758,
            "haversine":2793.4460842700964
        },
        {
            "start":(82.502038, -62.452469),
            "end":(35.316250, -101.574564),
            "bearing":198.29089010817097,
            "haversine":5451.147528030209
        }
    ]
    for case in cases:
        bearing = agf.gmaps.bearing(case["start"], case["end"])
        haversine = agf.gmaps.haversine(case["start"], case["end"])
        assert_floats_equal(case["bearing"], bearing, name="bearing")
        assert_floats_equal(case["haversine"], haversine, name="haversine")

def main():
    args = get_args()
    test_bearing_haversine(**args)
    pass

if __name__ == '__main__':
    main()
