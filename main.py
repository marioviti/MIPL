import cv2
import numpy
import scipy
import platform
import geometry
import utils
import image_signal
import morphology
import hierarchy
import contours_features

def main():
    print('python version: %s\nopencv verison: %s\nnumpy version: %s\nscipy version: %s' % (platform.python_version(), cv2.__version__, numpy.__version__,scipy.__version__))

def test():
    image = utils.read_image('test.png')
    resized = geometry.resize(image,fx=0.5,fy=0.125)
    utils.show_image(image)
    utils.show_image(resized)

if __name__ == "__main__":
    main()
    test()
