import cv2 as cv
import numpy as np

img = cv.imread('OpenCv/Photos/cats.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)