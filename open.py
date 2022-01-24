#importing the opencv module
import cv2

#imread() it take image path to work
img = cv2.imread(r'./images/Screenshot (56).png')

#imshow is using for display the image
cv2.imshow('image',img)

cv2.waitKey() # This is necessary to be required so that the image doesn't close immediately.
#It will run continuously until the key press.
cv2.destroyAllWindows()


# imwrite to save image
# status = cv2.imwrite("./images/cat.jpeg",img)
# print("Image written to file-system : ", status)

# accessing pixel (RGB)
pixel = img[400,400]
print(pixel)

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
size1 = img.size

print('Image height , width , channels : ', img.shape)
print('Image Height       : ', height)
print('Image Width        : ', width)
print('Number of Channels : ', channels)
print('Image Size  :', size1)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# loop runs if capturing has been initialized
while (1):

    # reads frames from a camera
    ret, frame = cap.read()

    # converting BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of red color in HSV
    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    # create a red HSV colour boundary and
    # threshold HSV image
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display an original image
    cv2.imshow('Original', frame)

    # discovers edges in the input image image and
    # marks them in the output map edges
    edges = cv2.Canny(frame, 100, 200)

    # Display edges in a frame
    cv2.imshow('Edges', edges)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    # Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()


im = cv2.imread(r'C:\Users\DEVANSH SHARMA\cat_16x9.jpg')
cv2.imshow('Original Image',im)
cv2.imshow('Blurred Image', cv2.blur(im, (3,3)))
cv2.waitKey(0)
cv2.destroyAllWindows()

# apply gaussian blur on src image
dst = median = cv2.medianBlur(img,5)
# display input and output image
cv2.imshow("Gaussian Smoothing", numpy.hstack((src, dst)))
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

# capture frames from a camera
cap = cv2.VideoCapture(0)

# loop runs if capturing has been initialized
while (1):

    # reads frames from a camera
    ret, frame = cap.read()

    # converting BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of red color in HSV
    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    # create a red HSV colour boundary and
    # threshold HSV image
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display an original image
    cv2.imshow('Original', frame)

    # discovers edges in the input image image and
    # marks them in the output map edges
    edges = cv2.Canny(frame, 100, 200)

    # Display edges in a frame
    cv2.imshow('Edges', edges)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    # Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()