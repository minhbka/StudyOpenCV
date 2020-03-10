import cv2
import numpy as np
from matplotlib import pyplot as plt

img_file_name = "opencv.png"
img = cv2.imread(img_file_name)
img2 = img[:, :, ::-1]
res_img = cv2.resize(img, (200, 200))

print(img.shape)

# show image by cv2
cv2.imshow('image', img)
cv2.imshow('image2', img2)
cv2.imshow('res', res_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# show image by matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

