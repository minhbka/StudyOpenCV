import numpy as np
import cv2

cap = cv2.VideoCapture(r".\vtest.mp4")

while cap.isOpened():
    ret, frame = cap.read()

    # change color
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    try:
        res_frame = cv2.resize(frame, (1280, 720))
    except Exception as e:
        print(str(e))
    # cv2.imshow('frame', frame) # show original
    # cv2.imshow('frame', frame) # show gray

    # show resized video
    cv2.imshow('frame', res_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


