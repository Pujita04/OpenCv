import cv2 as cv

img = cv.imread('OpenCv/Photos/park.jpg')

cv.imshow('Park', img)

# Converting an image to grayscale and hsv
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('Gray', gray)
# cv.imshow('HSV', hsv)

# Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
median = cv.medianBlur(img,5)
cv.imshow('Blur', blur)
cv.imshow('Median', median)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)
#to reduce the number of edges we can pass blur image

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation= cv.INTER_AREA)
# cv.imshow('REsize', resized)

# cropping
cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)


cv.waitKey(0)