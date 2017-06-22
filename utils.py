import cv2

def heightAndWidth(img):
    return img.shape[0:2]

def show_image(image,window='image'):
    cv2.imshow(window,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_image(path):
    """
    load as UNIT8 image
    """
    return cv2.imread(path)

def draw_contours(img,cnts, color=(0,255,0)):
    cv2.drawContours(img, cnts, -1, color , 3)
    return image
