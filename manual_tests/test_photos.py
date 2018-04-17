#!/usr/bin/env python3

from _test_base import *
import argparse
import agf.photos

def get_args():
    parser = argparse.ArgumentParser()
    # parser.add_argument("-k", "--key", required=True,
    #                 help="Google Maps developer API key.")
    return vars(parser.parse_args())

def simple_rgb_pixel_categorizer(R, G, B):
    if R > G:
        if R > B:
            return "R"
        elif B > R:
            return "B"
        else:
            return "RB"
    elif G > R:
        if G > B:
            return "G"
        elif B > G:
            return "B"
        else:
            return "GB"
    else:
        if B > R:
            return "B"
        elif R > B:
            return "RG"
        else:
            return "RGB"
        
def test_pixel_categorizer(*args, **kwargs):
    path_to_file = data_path("grass.jpg")
    expected_pixel_count = {"B": 14130,"G": 1893581,"GB": 2189,"R": 8081,"RB": 26,"RG": 1865,"RGB": 128}
    actual_pixel_count = agf.photos.categorize_pixels(path_to_file, simple_rgb_pixel_categorizer)
    assert_dicts_equal(expected_pixel_count, actual_pixel_count, name="counting pixels per color in grass.jpg")

def main():
    args = get_args()
    test_pixel_categorizer(**args)
    pass

if __name__ == '__main__':
    main()
