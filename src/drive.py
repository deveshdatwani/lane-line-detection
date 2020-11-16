import cv2
import numpy as np

cap = cv2.VideoCapture('../data/car3.mp4')
lower_white = np.array([190,150,150])
upper_white = np.array([255,255,255])

#region of interest
Y1 = 300
Y2 = 650
X1 = 215
X2 = 400

#processing the image

class image_processor():
    
    def resize(self, frame):

        frame = cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2))
        return frame

    def gaus_blur(self, frame, kernel_size=(5,5)):

        frame = cv2.GaussianBlur(frame, kernel_size, 5)
        return frame

process = image_processor()

#displaying the video
while cap.isOpened():
    ret, frame = cap.read()
    image = frame.copy()
    frame = process.resize(frame)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = process.resize(image)
    image_roi = image[X1:X2, Y1:Y2] 
    edges = cv2.Canny(image_roi, 50,150)
    
    #mask the image with white colour
    mask = cv2.inRange(frame, lower_white, upper_white)

    #applying gaussian blur to the roi
    g_blur = process.gaus_blur(edges)
   
    minLineLength = 100
    maxLineGap = 10
    line_detect = cv2.HoughLinesP(g_blur, 1, np.pi/180, threshold = 10, minLineLength =10, maxLineGap=5)
    
    #print(line_detect[0][0])
    #print(len(line_detect[0][0]))
    x1, y1, x2, y2 = line_detect[0][0]
    
    cv2.line(frame, (Y1+x1,X1+y1), (Y2+x2,X2+y2), (0,0,255), 2)

    #edges = cv2.bitwise_and(frame, frame, mask=mask)
    image[X1:X2, Y1:Y2] = g_blur

    cv2.imshow('original', frame)
    cv2.imshow('frame', image)
    
     
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
