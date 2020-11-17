import cv2 
import numpy as np

cap = cv2.VideoCapture('../data/car6.mp4') 
lower_white = np.array([190,150,150]) 
upper_white = np.array([255,255,255])

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

        lines_detected = cv2.HoughLinesP(image, 2, np.pi / 180, 100,np.array([]), minLineLength = 10, maxLineGap = 50) 
        
        return lines_detected

class lane_process():

    def cal_lines(self, hough, segment):

        left = [] 
        right = []

        for line in hough:
           
            x1, y1, x2, y2 = line[0] 
            line_parameters = np.polyfit((x1,x2), (y1,y2), 1) 
            slope = line_parameters[0] 
            y_intercept =line_parameters[1]

            if slope < 0: 
                left.append((slope, y_intercept)) 
            else:
                right.append((slope, y_intercept))
        
        left_avg = np.average(left, axis=0) 
        right_avg = np.average(right,  axis=0)
        left_line = line_calculate.calculate_coordinates(segment, left_avg)
        right_line = line_calculate.calculate_coordinates(segment, right_avg)
        
        return np.array([left_line, right_line])

    def calculate_coordinates(self, segment, parameters):

        slope, intercept = parameters 
        y1 = segment.shape[0] 
        y2 = int(y1 - 150)
        x1 = int((y1 - intercept) / slope) 
        x2 = int((y2 - intercept) / slope)

        return np.array([x1, y1, x2, y2])

    def visualize(self, lines, frame):

        lines_visualize = np.zeros_like(frame)

        if lines is not None:

            for x1, y1, x2, y2  in lines:

                cv2.line(lines_visualize, (x1,y1), (x2,y2), (0,255,0), 5)

        return lines_visualize


#initialising the image processor object 
process = image_processor()

#initialsing the line calcultor 
line_calculate = lane_process() 

#displaying the video 
while cap.isOpened():

    ret, frame = cap.read() 
    image = frame.copy() 
    frame = process.resize(frame)
    image = process.resize(image) 
    height = process.im_height(image) 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #hardcoding region of interest 
    ones = np.zeros_like(image)
    polygon = np.array([[(X1, height-140),(X2, height-140),(X3, Y3)]])
    cv2.fillConvexPoly(ones, polygon, (255,255,255)) 
    segment = cv2.bitwise_and(image, ones) 
    
    #processing the segment
    segment = process.im_canny(segment) 
    hough_line = process.hough_lines(segment)
 
    #all_lines = line_calculate.cal_lines(hough=hough_line, segment=segment)
    #segment = line_calculate.visualize(all_lines, frame)
    
    for pts in hough_line:
        
        x1,y1,x2,y2 = pts[0]
        points = np.array([[x1,y1],[x2,y2]])
        cv2.polylines(frame, [points], 1, (0,0,255), 5)

    cv2.imshow('original', frame) 
    cv2.imshow('segment', segment) 
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
