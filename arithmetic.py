import cv2 as cv 
import numpy as np

img1 = cv.imread('OpenCv/Photos/park.jpg')
img2 = cv.imread('OpenCv/Photos/lady.jpg')

#images should be same size so first resize the image 
resized1 = cv.resize(img1, (500,500), interpolation= cv.INTER_AREA)
resized2 = cv.resize(img2, (500,500), interpolation= cv.INTER_AREA)

cv.imshow('Resized1', resized1)
cv.imshow('Resized2', resized2)


dst = cv.addWeighted(resized1, 0.7, resized2, 0.3, 0)
cv.imshow('Dst', dst)



cv.waitKey(0)