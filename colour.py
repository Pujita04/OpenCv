import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('OpenCv/Photos/park.jpg')

# cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()

# Converting an image to grayscale and hsv
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('Gray', gray)
cv.imshow('HSV', hsv)

#converting bgr to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# tracking hsv value 
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
print( hsv_green )

#converting bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# plt.imshow(rgb)
# plt.show()

#converting hsv to bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv--> bgr', hsv_bgr)


cv.waitKey(0)