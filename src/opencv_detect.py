import cv2 
import numpy as np

cap = cv2.VideoCapture('../data/car6.mp4') 

#cordinates of ROI 
X1 = 180 
X2 = 850 
X3 = 460 
Y3 = 210

#creating image processor

class image_processor():
    
    def resize(self, frame):

        frame = cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2))        
        return frame

    def gaus_blur(self, frame, kernel_size=(5,5)):

        frame = cv2.GaussianBlur(frame, kernel_size, 5) 
        return frame
    
    def im_height(self, image):

        height = image.shape[0]         
        return height

    def im_canny(self, image):
        
        image = cv2.Canny(image, 50, 150)       
        return image

    def hough_lines(self, image):

        lines_detected = cv2.HoughLinesP(image, 2, 
                                        np.pi / 180, 100, 
                                        np.array([]), 
                                        minLineLength = 10, 
                                        maxLineGap = 50) 
        return lines_detected

class lane_processor():

    def lane_visuals(self, hough_lines):
        
        if hough_line is not None:     
            for pts in hough_line:

                x1,y1,x2,y2 = pts[0]
                points = np.array([[x1,y1],[x2,y2]])
                cv2.polylines(frame, [points], 1, (0,0,255), 5)
        
        else:
            cv2.putText(frame, 'No Lanes Detected',(300,400), 
                        cv2.FONT_HERSHEY_COMPLEX ,1, 
                        (0,255,255), 3)      
        return None

#initialising the image processor object 
process = image_processor()

#initialsing the line calcultor 
line_calculate = lane_processor() 

#process and display video file
while cap.isOpened():

    ret, frame = cap.read() 
    image = frame.copy() 

    #resizing, grayscaling the image
    frame = process.resize(frame)
    image = process.resize(image) 
    height = process.im_height(image) 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, 50, 150)

    #hardcoding region of interest 
    ones = np.zeros_like(image)
    polygon = np.array([[(X1, height-150),(X2, height-150),(X3, Y3)]])
    cv2.fillConvexPoly(ones, polygon, (255,255,255), 0) 
    segment = cv2.bitwise_and(image, ones)
    
    #processing the segment and visualising lanes
    segment = process.im_canny(segment) 
    hough_line = process.hough_lines(segment)     
    line_calculate.lane_visuals(hough_line)

    cv2.imshow('original', frame) 
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows() 
        break
