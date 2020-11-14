import cv2
import numpy as np

#loading the image
image = cv2.imread('../data/screenshot1.png')
img_copy = image.copy()

#creating a mask
lower_white = np.array([0,0,255])
upper_white = np.array([255,255,255])

#Reduce noise
blur = cv2.GaussianBlur(image, (5,5), 0)

#masking the frame and displaying
image_white = cv2.inRange(img_copy, lower_white, upper_white)
image_white = cv2.resize(image_white, (960, 540))

filename = '../data/screenshotdetect.png'
#edge detection 
edges = cv2.Canny(img_copy, 50, 150)
edges = cv2.resize(edges, (960, 540))
cv2.imwrite(filename, edges)

cv2.imshow('white lanes', edges)
if cv2.waitKey() == ord('q'):
    image.release()
    cv2.destroyAllWindows()

