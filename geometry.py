import cv2

def resize(image,fx=0.5,fy=0.5):
    M = int(1./fx)      #,MaxWx = 1./2.*M # in frequency domain
    N = int(1./fy)      #,MaxWy = 1./2.*N
    blurred = cv2.GaussianBlur(image,((2*M)-1,(2*N)-1),0)
    resized = cv2.resize(blurred,None,fx=fx,fy=fy,interpolation=cv2.INTER_NEAREST)
    return resized

def get_perspective_transform(src,dst):
    T = cv2.getPerspectiveTransform(src, dst)
    return T

def get_homography_transform(src,dst,method=cv2.RANSAC, ransacReprojThreshold=5.0):
    """
    src, dst: lists of points.
    """
    if method==cv2.RANSAC or method==CV_LMEDS:
        H, mask = cv2.findHomography(src_pts, dst_pts, method=method, ransacReprojThreshold=ransacReprojThreshold)
        return H, mask
    else:
        H = cv2.findHomography(src_pts, dst_pts, method=method, ransacReprojThreshold=ransacReprojThreshold)
        return H, None

def warp_perspective(image, M, shape=(0,0)):
    (maxWidth,maxHeigth) = shape
    if (maxWidth,maxHeigth) == (0,0):
        (maxWidth,maxHeigth) = image.shape
    warped_image = cv2.warpPerspective(image, M, (maxWidth,maxHeight))
    return warped_image

def perspective_transform(pts,M):
    dst = cv2.perspectiveTransform(pts,M)
    return dst

def get_rotation_matrix(angle,center,isotropic_scale_factor=1.0):
    RM = cv2.getRotationMatrix2D(center,angle,isotropic_scale_factor)
    return RM

def rotate_image(img, angle):
    RM = get_rotation_matrix(angle,(cols/2,rows/2))
    rotated_img = warp_perspective(img,RM)
    return rotated_img
