import cv2

"""
RGB space NOTE: Opencv orders channels as BGR - 012
"""

def convert_to_HSV(image):
    """
    convert image to HSV color space
    """
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
