import cv2

# load two images

img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('opencv-logo.png')

# create ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img1 = img1[50:rows + 50, 50 : cols + 50]
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

# # Now create a mask of logo and create its inverse mask also
# img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)
#
# # Now black-out the area of logo in ROI
# img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
#
# # Take only region of logo from logo image.
# img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
#
# # Put logo in ROI and modify the main image
# dst = cv2.add(img1_bg, img2_fg)
# img1[0:rows, 0:cols] = dst

# cv2.imshow('res', img1)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
