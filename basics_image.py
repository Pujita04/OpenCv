import cv2 as cv 
import numpy as np

img = cv.imread('OpenCv/Photos/park.jpg')
cv.imshow('Park', img)

#1. accessing pixel values
px = img[100,100]
blue = img[100,100,0]    # blue pixel
print(px)
print(blue)
# print(img.item(10,10,2))


#2.image shape:tells about the shape of image. Returns no of rows, columns, and channels
print(img.shape)

#3. img size: total number of pixels
print(img.size)

#4. img dtype : image datatype
print(img.dtype)

#5. ROI : region of image 
ball = img[240:300, 300:330]
# cv.imshow('BAll', img)

#6. creating a border around image
constant= cv.copyMakeBorder(img,2,2,2,2,cv.BORDER_CONSTANT, value=(0,0,0))
replicate = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_WRAP)

cv.imshow('Constant', constant)
cv.imshow('Replicate', replicate)
cv.imshow('Reflect', reflect)
cv.imshow('Reflect101', reflect101)
cv.imshow('WRap', wrap)



cv.waitKey(0)