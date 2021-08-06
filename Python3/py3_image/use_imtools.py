#!/usr/bin/env python

from PIL import Image
from numpy import *
## error
# from . import imtools

def histeq(im,nbr_bins=256):

    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1]
    im2 = interp(im.flatten(),bins[:-1],cdf)

    return im2.reshape(im.shape), cdf



im = array(Image.open('for_learn.jpeg').convert('L'))
## eror
# im2, cdf = imtools.histeq(im)

im2, cdf = histeq(im)
