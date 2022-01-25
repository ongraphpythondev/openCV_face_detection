
import cv2 as cv

def rescale_frame(frame , scale = 0.5):
    height = int(frame.shape[1] * scale)
    width = int(frame.shape[0] * scale)
    dimension = (width , height)

    # resize function resize it
    return cv.resize(frame , dimension , interpolation= cv.INTER_AREA)


# Read in an image
img = cv.imread('../images/Screenshot (57).png')
cv.imshow('Park', img)
small_image = rescale_frame(img , scale=.2)
cv.imshow("small image", small_image)

cv.waitKey(0)  # it will wait the screen

# for video
# capture = cv.VideoCapture('../images/h.mp4')
capture = cv.VideoCapture(0)# is opened previously or not

while True:
    isTrue , frame = capture.read()
    
    small_video = rescale_frame(frame , scale = .2)
    cv.imshow('video', frame)
    cv.imshow("small video", small_video)

    if cv.waitKey(20) & 0xFF == ord("c"):
        break

capture.release()
cv.destroyAllWindows()