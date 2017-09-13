"""Image statistics"""
import numpy as np
import views

def intensity_histogram(image_channel, bins=256, density=True):
    return np.histogram(image_channel, bins=bins, density=density)
