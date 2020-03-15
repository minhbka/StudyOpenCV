import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi.jpg')
lower_reso = cv2.pyrDown(img)

plt.imshow(lower_reso), plt.title('lowreso')
plt.xticks([]), plt.yticks([])
plt.show()