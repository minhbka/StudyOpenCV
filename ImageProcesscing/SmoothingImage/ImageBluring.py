import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo.png')
# Average Blur
av_blur = cv2.blur(img, (5,5))

# Gaussian Blur
g_blur = cv2.GaussianBlur(img,(5,5),0)

# add Gaussian noise

row, col, ch = img.shape
mean = 0
var = 0.1
sigma = var**0.5
gauss = np.random.normal(mean,sigma,(row,col,ch))
gauss = gauss.reshape(row, col, ch)
noisy = img + gauss
noisy = np.clip(noisy, 0, 255)
noisy = np.float32(noisy)

median_blur = cv2.medianBlur(noisy, 5)

b_blur = cv2.bilateralFilter(noisy,9,75,75)

plt.subplot(231), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(av_blur), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(g_blur), plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.subplot(234), plt.imshow(noisy), plt.title('With Noise')
plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(median_blur), plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.subplot(236), plt.imshow(b_blur), plt.title('Bilateral')
plt.xticks([]), plt.yticks([])
plt.show()

