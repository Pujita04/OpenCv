import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')  #creating blank image 
# cv.imshow('Blank', blank)

#1.Paint the image a certain colour
# blank[:] = 255,25,156             #rgb value for colour  
# cv.imshow('Painted image', blank)


#2. Draw a rectangle
# cv.rectangle(blank, (15,15), (250,250), (0,255,0), thickness = 2)
# cv.imshow('Rectangle', blank)
#for filling the colour: thickness = -1 or cv.filled
#instead  of (300,250) I can write (blank.shape[1]//2, blank.shape[0]//2)


#3. Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness = -1)
# cv.imshow('Circle', blank)

#4. Draw a line
# cv.line(blank, (0,0), (250,250), (255,255,255), thickness=2)
# cv.imshow('Line', blank)

#5. Write text
cv.putText(blank, 'Hello Pujita', (100,150), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)



cv.waitKey(0)