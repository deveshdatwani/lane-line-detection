import cv2
import numpy as np

cap = cv2.VideoCapture('drive.mp4')
lower_white = np.array([0,0,255])
upper_white = np.array([255,255,255])
 
while cap.isOpened():
    ret, frame = cap.read()
    image = frame.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_white = cv2.inRange(frame, lower_white, upper_white)
    sobely = cv2.Sobel(image_white, cv2.CV_64F, 0, 1, ksize=5)
    #edges = cv2.Canny(image, 50,150)
    if ret == True:
        cv2.imshow('frame', sobely)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
