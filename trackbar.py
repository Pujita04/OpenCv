import cv2 as cv
import numpy as np

def nothing(x):
    pass

#creating a blank image and window
img = np.zeros((500,500,3), dtype= 'uint8')
cv.namedWindow('image')

# create trackbars for color change
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)

#creating switch for on/off functionality
switch = '0:OFF \n 1:ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
 cv.imshow('image',img)
 k = cv.waitKey(1) & 0xFF
 if k == 27:
  break


 # get current positions of four trackbars
 r = cv.getTrackbarPos('R','image')
 g = cv.getTrackbarPos('G','image')
 b = cv.getTrackbarPos('B','image')
 s = cv.getTrackbarPos(switch,'image')

 if s == 0:
  img[:] = 0
 else:
  img[:] = [b,g,r]

  
cv.destroyAllWindows()

