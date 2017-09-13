import cv2
import numpy as np

"""
RGB space NOTE: Opencv orders channels as BGR - 012
Datatype and pixels in opencv/numpy

    VAL Interv   |   Opencv  ->  numpy
    ---------------------------------------
    0   to 255   |   CV_8U   ->  np.uint8
    0   to 65535 |   CV_16U  ->  np.uint16
    0.f to 1.f   |   CV_32F  ->  np.float32
    ----------------------------------------
"""

def convert_BGR_to_RGB(image):
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return rgb_image

def add_channel(image):
    """ add new array in third dimension """
    new_channel = np.ones(image[:,:,0].shape,dtype=np.uint8)*255
    return np.dstack((image,new_channel))

def swap_channels(image,a,b, inplace=True):
    temp = np.copy(image[:,:,a])
    image[:,:,b] = image[:,:,a]
    image[:,:,a] = temp
    return image

def normalize_pixels(image, l0=0., l1=1.0):
    """ Change range of pixel intensity values to [l0-l1],
    notice that you can invert the image by setting l0 = 1 and l1 = 0,
    but it is a waste of time """
    _min,_max = np.min(image), np.max(image)
    ranges_ratio = (l1-l0)/(_max-_min)
    b = l0 - (_min * (ranges_ratio))
    a = ranges_ratio
    normalized_pixel_image = image*a + b
    return normalize_pixels

def invert_pixels(image):
    """Invert pixels values original range (conservative)"""
    _min,_max = np.min(image), np.max(image)
    b = _max - _min
    inverted_pixel_image =  b - image
    return inverted_pixel_image

def convert_to_HSV(image):
    """convert RGB(BGR in opencv numpy) to HSV color space"""
    hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    return hsv_image

def convert_to_grey(image):
    """
    VAL Interv   |   Opencv  ->  numpy
    ---------------------------------------
    0   to 255   |   CV_8U   ->  np.uint8
    0   to 65535 |   CV_16U  ->  np.uint16
    0.f to 1.f   |   CV_32F  ->  np.float32
    ----------------------------------------
    """
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray_image
