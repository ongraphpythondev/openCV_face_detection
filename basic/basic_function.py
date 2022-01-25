
import cv2 as cv

# Read in an image
img = cv.imread('../images/Screenshot (57).png')
cv.imshow('Park', img)

cv.waitKey(0)  # it will wait the screen

# for video
capture = cv.VideoCapture('../images/h.mp4')
while True:
    isTrue , frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord("c"):
        break

capture.release()
cv.destroyAllWindows()