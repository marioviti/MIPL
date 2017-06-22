import numpy as np
from scipy.signal import fftconvolve

def fft(img):
    f = np.fft.fft2(img)
    return f

def ifft(fft_img):
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back

def shift_spectrum(f):
    fshift = np.fft.fftshift(f)
    return fshift

def magnitude_spectrum(f):
    fm = 20*np.log(np.abs(f))
    return fm

def get_fft_magnitude_spectrum(img, fx=1.0, fy=1.0):
    if fx > 1.0 or fy > 1.0:
        temp = np.copy(img)
        x,y = temp.shape
        img = np.zeros((np.int0(x*fx),np.int0(y*fy)))
        img[:x,:y] = temp
    f = fft(img)
    ssf = shift_spectrum(f)
    fm = magnitude_spectrum(ssf)
    return fm

def fft_convolve(X, kernel):
    Y = fftconvolve(X, kernel, mode='same')
    return Y
