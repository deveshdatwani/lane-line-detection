import cv2
import numpy as np

cap = cv2.VideoCapture('../data/car6.mp4')
lower_white = np.array([190,150,150])
upper_white = np.array([255,255,255])
 
x1 = 200
x2 = 400
y1 = 200
y2 = 700

#processing the image 
def im_processor(frame):

    frame = cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2))
    return frame

#display
while cap.isOpened():
    ret, frame = cap.read()
    image = frame.copy()
    frame = im_processor(frame)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = im_processor(image)
    image_roi = image[x1:x2, y1:y2] 
    #edges = cv2.Canny(image_roi, 50,150)
    
    #mask the image with white colour
    mask = cv2.inRange(frame, lower_white, upper_white)
    edges = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('original', frame)
    cv2.imshow('frame', edges)
    
    '''
    #cv2.rectangle(edges, (200,200), (700,400), (255,255,255), 2)
    image[x1:x2, y1:y2] = edges
    if ret == True:
        cv2.imshow('frame', image)
        cv2.imshow('frame1', frame)'''
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
