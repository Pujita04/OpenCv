import cv2 as cv
import numpy as np

img = cv.imread('OpenCv/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('Masked', masked)

masked2 = cv.bitwise_or(img, img, mask=mask)
cv.imshow('Masked2', masked2)

cv.waitKey(0)
