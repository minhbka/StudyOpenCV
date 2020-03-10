import numpy as np
import cv2  #3.0.0-dev
import math

r1 = 70
r2 = 30

ang = 60

d = 170
h = int(d/2*math.sqrt(3))

dot_red = (256, 128)
dot_green = (int(dot_red[0]-d/2), int(dot_red[1]+h))
dot_blue = (int(dot_red[0]+d/2), int(dot_red[1]+h))

# tan = float(dot_red[0]-dot_green[0])/(dot_green[1]-dot_red[0])
# ang = math.atan(tan)/math.pi*180

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
black = (0, 0, 0)

full = -1

img = np.zeros((512, 512, 3), np.uint8)
print(dot_green, dot_red, dot_blue)
cv2.circle(img, dot_red, r1, red, -1)
cv2.circle(img, dot_green, r1, green, -1)
cv2.circle(img, dot_blue, r1, blue, -1)
cv2.circle(img, dot_red, r2, black, -1)
cv2.circle(img, dot_green, r2, black, -1)
cv2.circle(img, dot_blue, r2, black, -1)
#
cv2.ellipse(img, dot_red, (r1, r1), ang, 0, ang, black, -1)
cv2.ellipse(img, dot_green, (r1, r1), 360-ang, 0, ang, black, -1)
cv2.ellipse(img, dot_blue, (r1, r1), 360-2*ang, ang, 0, black, -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),4,cv2.LINE_AA)

cv2.imshow("opencv_logo.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()