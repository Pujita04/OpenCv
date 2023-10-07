import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')  #creating blank image 
# cv.imshow('Blank', blank)

#1.Paint the image a certain colour
# blank[:] = 255,25,156             #rgb value for colour  
# cv.imshow('Painted image', blank)


#2. Draw a rectangle
cv.rectangle(blank, (15,15), (300,250), (0,255,0), thickness = 2)
cv.imshow('Rectangle', blank)



# img = cv.imread('OpenCv/Photos/cat.jpg')

# cv.imshow('CAt', img)

cv.waitKey(0)