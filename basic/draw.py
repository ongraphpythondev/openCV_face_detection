import cv2 as cv
from cv2 import circle
import numpy as np


# this will create blank screen where we can draw
blank = np.zeros((500,500 , 3) , dtype="uint8")
cv.imshow("Blank screen" , blank)

# to color in a certain portion of screen
blank[200:400 , 200:400] = 0,0,255
cv.imshow("Blank screen" , blank)

# to draw rectangle
cv.rectangle(blank , (0,20) , (200  ,500), (0,200,0), thickness=-1)
cv.imshow("rectangle", blank)

# to draw cirle
cv.circle(blank , (blank.shape[1]//2 , blank.shape[0]//2 ) , 50 , (200,0,0) , thickness=-1 )
cv.imshow("circle" , blank)

# Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)


# Write text
cv.putText(blank, 'Hello, my name is ritesh!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.imshow("rectangle", blank)


cv.waitKey(0)