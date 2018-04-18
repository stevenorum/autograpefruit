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

def test_image_average_color(*args, **kwargs):
    path_to_file = data_path("grass.jpg")
    expected_rgb = (78, 137, 92)
    actual_rgb = agf.photos.image_average_color(agf.photos.load_image(path_to_file))
    assert_lists_equal(expected_rgb, actual_rgb, name="average RGB color of image")

def test_chunkify(*args, **kwargs):
    path_to_file = data_path("grass.jpg")
    expected_colors = [
        (80, 141, 94), (83, 146, 100), (82, 143, 95), (82, 144, 94),
        (76, 134, 89), (83, 137, 97), (81, 136, 94), (74, 131, 88),
        (68, 127, 85), (62, 119, 79), (66, 127, 86), (54, 114, 73)
    ]
    chunks = agf.photos.chunkify_image(path_to_file, 500)
    actual_colors = []
    for chunk in chunks:
        actual_colors.append(agf.photos.image_average_color(chunk))
    assert_lists_equal(expected_colors, actual_colors, name="chunking up an image")

def main():
    args = get_args()
    test_pixel_categorizer(**args)
    test_image_average_color(**args)
    test_chunkify(**args)
    pass

if __name__ == '__main__':
    main()
