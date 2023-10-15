import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('OpenCv/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray)

#grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.xlim([0,256])
plt.plot(gray_hist)
plt.show()






cv.waitKey(0)