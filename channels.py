import numpy as np
import skimage
from skimage import io,filters

def get_rgb_channels(image):
    r_channel = image[:, :, 0]
    g_channel = image[:, :, 1]
    b_channel = image[:, :, 2]
    return r_channel, g_channel, b_channel


def join_rgb_channels(r_channel, g_channel, b_channel):
    return np.stack([r_channel, g_channel, b_channel], axis=2)


def customize_channel(channel, values):
    original_size = channel.shape
    flat = channel.flatten()
    customized = np.interp(flat,np.linspace(0, 1, len(values)), values)
    return customized.reshape(original_size)

def sharper_image(image,a,b,sigma=10):
    blurred  = filters.gaussian(image, sigma=sigma,multichannel=True)
    sharper = np.clip(image*a - blurred*b,0,1.0)
    return sharper



