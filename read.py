import cv2 as cv

# img = cv.imread('OpenCv/Photos/cat.jpg')

# cv.imshow('Cat', img)

capture = cv.VideoCapture('OpenCv/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)  #this statement means that the image or video will display forever until some key is pressed
