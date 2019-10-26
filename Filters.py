import channels
import numpy as np
import cv2
from matplotlib import pyplot as plt

def heather_filter(image):
    r, g, b = channels.get_rgb_channels(image)
    r_0 = channels.customize_channel(r, [
    0, 0.2, 0.3, 0.5, 0.6,
    0.75, 0.8, 0.85, 0.9,
    0.95, 1.0])
    bluer_black_px = channels.join_rgb_channels(r_0, g, np.clip(b+0.03,0,1.0))
    sharper = channels.sharper_image(bluer_black_px, 1.3, 0.3, sigma=10)
    b = sharper[:, :, 2]
    b_0 = channels.customize_channel(b, [
    0, 0.047, 0.118, 0.251, 0.318,
    0.392, 0.42, 0.439, 0.475,
    0.52, 0.58, 0.6, 0.65,
    0.7, 0.75, 0.8, 1])
    sharper[:, :, 2] = b_0
    return sharper


def blur(img):
    gaussian_blur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
    return plt.imshow(gaussian_blur)


def canny_edges(img):
    detected_edges = cv2.Canny(img, 100, 300)
    return plt.imshow(detected_edges, cmap='gray')