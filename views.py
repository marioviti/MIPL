import numpy as np
import scipy
import scipy.special
import color_spaces

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

def image_for_bokeh(image):
    if len(image.shape) > 2:
        image_bokeh = color_spaces.convert_BGR_to_RGB(image)
        image_bokeh = color_spaces.add_channel(image_bokeh)
        image_bokeh[:,:,0] = image_bokeh[:,:,0].T[:,::-1].T
        image_bokeh[:,:,1] = image_bokeh[:,:,1].T[:,::-1].T
        image_bokeh[:,:,2] = image_bokeh[:,:,2].T[:,::-1].T
    else:
        image_bokeh = image.T[:,::-1].T
    return image_bokeh

def image_view(image):
    image_bokeh = image_for_bokeh(image)
    max_d = np.max(image.shape)
    plot_image = figure(x_range=(0, (image_bokeh.shape[0]/float(max_d)*10)), y_range=(0, (image_bokeh.shape[1]/float(max_d))*10))
    if len(image.shape) > 2: # colored image
        plot_image.image_rgba(image=[image_bokeh], x=0, y=0, dw=10, dh=10)
    else:
        plot_image.image(image=[image_bokeh], x=0, y=0, dw=10, dh=10)
    return plot_image

def histogram_view(image,bins=256):
    plot_image = image_view(image)
    if len(image.shape) > 2: # colored image
        histogram_plots = []
        channels=["red","green","blue"]
        for channel in range(3):
            histrogram_obj = np.histogram(image[:,:,channel], bins=bins, density=True)
            hist, edges  = histrogram_obj
            histogram_plot = figure(\
                    title="Histogram pixels intesity of channel " \
                    + channels[channel], background_fill_color="#E8DDCB")
            histogram_plot.quad(top=hist, bottom=0,
                left=edges[:-1], right=edges[1:],
                fill_color="#036564", line_color="#033649")
            histogram_plot.yaxis.axis_label = 'P(x)'
            histogram_plot.xaxis.axis_label = '(x)'
            histogram_plots += [histogram_plot]
        show(gridplot(plot_image, *histogram_plots, ncols=4,  \
            toolbar_location="below", toolbar_sticky=False))
    else:
        hist, edges  = histrogram_obj
        histogram_plot = figure(title="Histogram pixels intesity",
                background_fill_color="#E8DDCB")
        histogram_plot.quad(top=hist, bottom=0,
            left=edges[:-1], right=edges[1:],
            fill_color="#036564", line_color="#033649")
        histogram_plot.yaxis.axis_label = 'P(x)'
        histogram_plot.xaxis.axis_label = '(x)'
        show(gridplot(plot_image, histogram_plot, ncols=2,  \
            toolbar_location="below", toolbar_sticky=False))
    output_file("image_rgba.html")
