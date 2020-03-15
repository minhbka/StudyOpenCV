import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('dave.jpg')

laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0, ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1, ksize=5)
sobel = cv2.Sobel(img,cv2.CV_64F,1,1, ksize=5)

plt.subplot(2,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5),plt.imshow(sobel,cmap = 'gray')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])
plt.show()