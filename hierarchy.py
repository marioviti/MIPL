import geometry
import utils

# Some history
# http://docs.opencv.org/3.1.0/dc/dff/tutorial_py_pyramids.html

def pyrDown(image):
    return cv2.pyrDown(image)

def pyrUp(image):
    return cv2.pyrUp(image)

def build_pyramid(img, levels, eps = 10):
    i = 0
    pyramid = []
    curr_level = img
    height, width = utils.heightAndWidth(curr_level)
    while( i<levels and width<eps and height<eps ):
        next_level = geometry.resize(curr_level)
        pyramid += [next_level.copy()]
        curr_level = next_level
        height, width = utils.heightAndWidth(curr_level)
        i+=1
    return pyramid
