import cv2
import numpy as np

# Moments operations

def moments(cnt):
    # 0 - 3rd order moments
    M = cv2.moments(cnt)
    return M

def center(cnt,M=None):
    if M == None:
        M = moments(cnt)
    cx = int(M['m10']/M['m00']) # aka mean on x
    cy = int(M['m01']/M['m00']) # aka mean on y
    return cx,cy,M

def area(cnt,M=None):
    if M==None:
        M = moments(cnt)
    area = M['m00']
    return area, M

def perimeter(cnt):
    peri = cv2.arcLength(cnt,True)
    return peri

def contour_approx(cnt, epsilon=0.1):
    """
    Douglas-Peucker algorithm:
    approximate contour to match
    a fraction epsilon of the perimeter.
    """
    epsilon_per = epsilon*perimeter(cnt)
    approx = cv2.approxPolyDP(cnt,epsilon_per,True)
    return approx

def convex_hull(cnt, clockwise=True, returnPoints=True):
    """
    if returnPoints == False
    return the indexes in cnt of the points corresponding to the convexHull.
    """
    hull = cv2.convexHull(cnt, None, clockwise, returnPoints)
    return hull

def check_convexity(cnt):
    k = cv2.isContourConvex(cnt)
    return k

def min_fit_circle(cnt):
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    return center, radius

def fit_ellipse(cnt):
    ellipse = cv2.fitEllipse(cnt)
    return ellipse

def fit_line(cnt):
    [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
    return [vx,vy,x,y]

def bounding_box(cnt):
    rect= cv2.boundingRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    return box

def min_fit_box(cnt):
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    return box
