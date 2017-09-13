import utils
import numpy as np
import histograms as hs


def normalize_pixels(image,l0 = 0., l1 = 1.0):
    """ Change range of pixel intensity values to [l0-l1],
    notice that you can invert the image by setting l0 = 1 and l1 = 0,
    but it is a waste of time """
    _min,_max = np.min(image), np.max(image)
    ranges_ratio = (l1-l0)/(_max-_min)
    b = l0 - (_min * (ranges_ratio))
    a = ranges_ratio
    normalized_pixel_image = image*a + b
    return normalized_pixel_image


def invert_pixels(image):
    """Invert pixels values original range (conservative)"""
    _min,_max = np.min(image), np.max(image)
    b = _max - _min
    inverted_pixel_image =  b - image
    return inverted_pixel_image

if __name__=="__main__":
    image = utils.read_image('test.png')
    image_normalized = normalize_pixels(image,l0=1.,l1=0.)
    hs.view_intensity_histogram(image)
