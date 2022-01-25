#importing the opencv module
import cv2

#imread() it take image path to work
img = cv2.imread(r'./images/Screenshot (57).png')


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



# accessing pixel (RGB)
pixel = img[400,400]
print(pixel)

#imshow is using for display the image
cv2.imshow('image',img)

cv2.waitKey() # This is necessary to be required so that the image doesn't close immediately.
#It will run continuously until the key press.
cv2.destroyAllWindows()


# imwrite is used to save image
status = cv2.imwrite("./images/cat.jpeg",img)
print("Image written to file-system : ", status)

# change color of image
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )  
cv2.imshow("gray image", image)

cv2.waitKey() # This is necessary to be required so that the image doesn't close immediately.
#It will run continuously until the key press.
cv2.destroyAllWindows()


