import cv2 as cv

img = cv.imread('OpenCv/Photos/cats.jpg')
cv.imshow('Cats', img)

#Averaging
average = cv.blur(img, (3,3));
cv.imshow('Average', average)

#Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

#median blur --> highly effective in removing noises
median = cv.medianBlur(img, 5)
cv.imshow('Median Blur', median)

#bilateral blur--> retaining edges
bilateral = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)