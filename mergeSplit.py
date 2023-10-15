import cv2 as cv
import numpy as np

img = cv.imread('OpenCv/Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros((img.shape[:2]), dtype='uint8')

#spliting image into b, g, r images
b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

#better visualization of red, green, blue
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('REd', red)



#they will all shows greyscale images lighter portion --> high concentration of particular color. Darker portion--> less concentration
# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)

#printing image shape
print(img.shape)  #channel 3 represents three channels blue, green, red
print(b.shape)
print(g.shape)
print(r.shape)

#merge
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)