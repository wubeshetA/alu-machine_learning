#!/usr/bin/env python3
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import vgg19
from tensorflow.keras.preprocessing.image import img_to_array, load_img


class NST:
    style_layers = ['block1_conv1', 'block2_conv1',
                    'block3_conv1', 'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        if not isinstance(style_image, np.ndarray) or style_image.shape[-1] != 3:
            raise TypeError(
                "style_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(content_image, np.ndarray) or content_image.shape[-1] != 3:
            raise TypeError(
                "content_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(alpha, (int, float)) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if not isinstance(beta, (int, float)) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

        tf.compat.v1.enable_eager_execution()

    @staticmethod
    def scale_image(image):
        if not isinstance(image, np.ndarray) or image.shape[-1] != 3:
            raise TypeError(
                "image must be a numpy.ndarray with shape (h, w, 3)")

        image = tf.image.resize_with_crop_or_pad(image, 512, 512)
        image = tf.image.resize(
            image, (512, 512), method=tf.image.ResizeMethod.BICUBIC)
        image = tf.cast(image, tf.float32) / 255.0
        image = tf.expand_dims(image, axis=0)

        return image


# Usage
if __name__ == '__main__':
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt

    style_image = mpimg.imread("starry_night.jpg")
    content_image = mpimg.imread("golden_gate.jpg")

    print(NST.style_layers)
    print(NST.content_layer)
    nst = NST(style_image, content_image)
    scaled_style = nst.scale_image(style_image)
    scaled_content = nst.scale_image(content_image)
    print(type(nst.style_image), nst.style_image.shape,
          np.min(nst.style_image), np.max(nst.style_image))
    print(type(nst.content_image), nst.content_image.shape,
          np.min(nst.content_image), np.max(nst.content_image))
    print(nst.alpha)
    print(nst.beta)
    print(tf.executing_eagerly())
    assert (np.array_equal(scaled_style, nst.style_image))
    assert (np.array_equal(scaled_content, nst.content_image))

    plt.imshow(nst.style_image[0])
    plt.show()
    plt.imshow(nst.content_image[0])
    plt.show()
