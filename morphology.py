import numpy as np
import cv2

structuring_elements_types= {
    'rect' : cv2.MORPH_RECT,
    'ellipse' : cv2.MORPH_ELLIPSE,
    'cross' : cv2.MORPH_CROSS
}

def get_structing_el(el_strct_type):
    return cv2.getStructuringElement(structuring_elements_types[el_strct_type],(5,5))

def erode(img, kernel_type='rect', iterations=1):
    kernel = get_structing_el(kernel_type)
    erosion = cv2.erode(img,kernel,iterations = iterations)
    return erosion

def dilatate(img, kernel_type='rect', iterations=1):
    kernel = get_structing_el(kernel_type)
    dilation = cv2.dilate(img,kernel,iterations = iterations)
    return dilation

def open(img, kernel_type='rect'):
    """
    dilatation(erosion(img))
    """
    kernel = get_structing_el(kernel_type)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return opening

def close(img, kernel_type='rect'):
    """
    erosion(dilatation(img))
    """
    kernel = get_structing_el(kernel_type)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    return closing

def grad(img, kernel_type='rect'):
    """
    dilatation(img) - erosion(img)
    """
    kernel = get_structing_el(kernel_type)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    return gradient

def topHat(img, kernel_type='rect'):
    """
    opening(img)-img
    """
    kernel = get_structing_el(kernel_type)
    th = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    return th

def blackHat(img, kernel_type='rect'):
    """
    closing(img)-img
    """
    kernel = get_structing_el(kernel_type)
    bh = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    return bh
