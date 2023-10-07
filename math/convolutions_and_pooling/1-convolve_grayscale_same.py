#!/usr/bin/env python3
"""
Performs a valid convolution on grayscale 
if necessary, the image should be padded with 0’s
"""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """ Convolve image on grayscale images

    Args:
        images (ndarry): _description_
        kernel (ndarray): _description_
    """

    m, h, w = images.shape
    kh, kw = kernel.shape
    output_h = h
    output_w = w
    if kh % 2 == 0:
        output_h = h - kh + 1
    if kw % 2 == 0:
        output_w = w - kw + 1
    output = np.zeros((m, output_h, output_w))
    pad_h = kh // 2
    pad_w = kw // 2
    images = np.pad(images, ((0, 0), (pad_h, pad_h),
                    (pad_w, pad_w)), 'constant')
    for i in range(output_h):
        for j in range(output_w):
            output[:, i, j] = (kernel * images[:, i: i + kh, j: j + kw])\
                .sum(axis=(1, 2))
    return output
