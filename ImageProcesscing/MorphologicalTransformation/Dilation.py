import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
print(kernel)
dilation = cv2.dilate(img,kernel,iterations = 1)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dilation), plt.title('Dilation')
plt.xticks([]), plt.yticks([])
plt.show()
