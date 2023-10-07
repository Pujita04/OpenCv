#rescaling and resizing the image frame
import cv2 as cv

img = cv.imread('OpenCv/Photos/cat_large.jpg')

cv.imshow('Cat', img)


#function to change the resolution but works only for live videos
def changeRes(width, height):
    #Live videos
    capture.set(3, width)
    capture.set(4, height)


#function to resize the frame of video or image
def rescaleFrame(frame, scale = 0.2):
    # Images, Videos and live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

#Reading video 
capture = cv.VideoCapture('OpenCv/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)  #function calling 

    # cv.imshow('Video', frame)
    # cv.imshow('Video resized', frame_resized)  #video display

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)