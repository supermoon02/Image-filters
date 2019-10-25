import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

path = 'DSC_0257.JPG'
image = cv2.imread(path)


image_before = Image.open(path)
image_before.show()


def one(img):
    gaussian_blur = cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)
    return plt.imshow(gaussian_blur)


def edges(img):
    detected_edges = cv2.Canny(image, 100, 300)
    return plt.imshow(detected_edges)


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


f1 = plt.figure(1)
f1 = one(image)
f2 = plt.figure(2)
f2 = edges(image)

#f3 = plt.figure(3)
#f3 = vintage(image)
plt.show()
