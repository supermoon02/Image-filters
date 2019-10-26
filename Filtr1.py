import cv2
import matplotlib.pyplot as plt
import numpy as np
import skimage
from skimage import io
import Filters

path = 'DSC_0257.JPG'
image_cv2 = cv2.imread(path)
image = skimage.img_as_float(io.imread(path))
original_im = plt.figure(1)
original_im = plt.imshow(image)





def vintage(img):
    rows, cols = img.shape[:2]
    print(rows,cols)
    kernel_x = cv2.getGaussianKernel(rows,200)
    kernel_y = cv2.getGaussianKernel(cols,200)
    kernel = kernel_x * kernel_y.T
    filter = 255 * kernel / np.linalg.norm(kernel)
    vintage_img = np.copy(img)
    for i in range(3):
        vintage_img[:,:,i] = vintage_img[:,:,i]* filter
    return plt.imshow(vintage_img)

#f2 = plt.figure(2)
#f2 = Filters.canny_edges(image_cv2)
#f1 = plt.figure(3)
#f1 = Filters.blur(image_cv2)
f3 = plt.figure(3)
f3 = vintage(image_cv2)
#im_3 = plt.figure(4)
#im_3 = plt.imshow(Filters.heather_filter(image))
plt.show()

