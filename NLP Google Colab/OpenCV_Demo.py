# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 19:50:19 2020

@author: Rajesh
"""

# Import the Libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2


# Reading the Images.
image = cv2.imread('E:\OpenCV\Images\index.png')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# Plotting the Image.
plt.imshow(image)

# TO saving the Image.
cv2.imwrite('E:\OpenCV\Images\test_write.jpg',image)

"""
By default, the imread function reads images in the BGR (Blue-Green-Red) format. 
We can read images in different formats using extra flags in the imread function:

cv2.IMREAD_COLOR: Default flag for loading a color image
cv2.IMREAD_GRAYSCALE: Loads images in grayscale format
cv2.IMREAD_UNCHANGED: Loads images in their given format, including the alpha channel. 
Alpha channel stores the transparency information – the higher the value of alpha channel, 
the more opaque is the pixel
"""

"""
OpenCV reads a given image in the BGR format by default. 
So, you’ll need to change the color space of your image 
from BGR to RGB when reading images using OpenCV. Let’s see how to do that:
"""

# import the required libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import cv2 

image = cv2.imread('E:\OpenCV\Images\index.jpg') 
#converting image to Gray scale 
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#plotting the grayscale image
plt.imshow(gray_image) 
#converting image to HSV format
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
#plotting the HSV image
plt.imshow(hsv_image)


# Resizing Images
"""
Machine learning models work with a fixed sized input. 
The same idea applies to computer vision models as well. 
The images we use for training our model must be of the same size.
This operation is useful for training deep learning models 
when we need to convert images to the model’s input shape.
"""

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

#reading the image 
image = cv2.imread('E:\OpenCV\Images\index.jpg') 
#converting image to size (100,100,3) 
smaller_image = cv2.resize(image,(100,100),interpolation=cv2.INTER_LINEAR) 
#plot the resized image
plt.imshow(smaller_image)


# Image Rotation
"""
For most deep learning models, you need to have large image set 
and that can be done through data augmentation. 
Resize, crop, rotate etc. are the ways of data augmentation.

"""
#importing the required libraries 
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

image = cv2.imread('E:\OpenCV\Images\index.png') 
rows,cols = image.shape[:2] # rows = 321 , cols = 500
#(col/2,rows/2) is the center of rotation for the image 
# M is the cordinates of the center 
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1) 
dst = cv2.warpAffine(image,M,(cols,rows)) 
plt.imshow(dst)


# Image Translation
# importing the required libraries 
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

#reading the image
image = cv2.imread('E:\OpenCV\Images\index.png')
#shifting the image 100 pixels in both dimensions
M = np.float32([[1,0,-100],[0,1,-100]]) 
dst = cv2.warpAffine(image,M,(cols,rows)) 
plt.imshow(dst)



# Simple Image Thresholding
"""
Thresholding is an image segmentation method. 
It compares pixel values with a threshold value and 
updates it accordingly. 
OpenCV supports multiple variations of thresholding. 
A simple thresholding function can be defined like this:

if Image(x,y) > threshold , Image(x,y) = 1

else, Image(x,y) = 0
"""
# Thresholding can only be applied to grayscale images.

# importing the required libraries 
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 


#here 0 means that the image is loaded in gray scale format
gray_image = cv2.imread('E:\OpenCV\Images\index.png',0)

ret,thresh_binary = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
ret,thresh_binary_inv = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY_INV)
ret,thresh_trunc = cv2.threshold(gray_image,127,255,cv2.THRESH_TRUNC)
ret,thresh_tozero = cv2.threshold(gray_image,127,255,cv2.THRESH_TOZERO)
ret,thresh_tozero_inv = cv2.threshold(gray_image,127,255,cv2.THRESH_TOZERO_INV)

#DISPLAYING THE DIFFERENT THRESHOLDING STYLES
names = ['Original Image','BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
images = gray_image,thresh_binary,thresh_binary_inv,thresh_trunc,thresh_tozero,thresh_tozero_inv

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(names[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()


#Adaptive Thresholding
"""
In case of adaptive thresholding, different threshold values 
are used for different parts of the image.

No DEMO
"""

"""
Image Segmentation (Watershed Algorithm)
Image segmentation is the task of classifying every pixel in the image to some class. 
For example, classifying every pixel as foreground or background. 
Image segmentation is important for extracting the relevant parts from an image.
NO DEMO
"""

#Bitwise Operations
"""
Bitwise operations include AND, OR, NOT and XOR. 
You might remember them from your programming class! 
In computer vision, these operations are very useful 
when we have a mask image and want to apply that 
mask over another image to extract the region of interest.
"""


#import required libraries
import numpy as np 
import matplotlib.pyplot as plt 
import cv2 
 
#read the image
image = cv2.imread('E:\OpenCV\Images\coins.jpg')
#apply thresholdin 
ret,mask = cv2.threshold(sure_fg,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) 
#apply AND operation on image and mask generated by thrresholding
final = cv2.bitwise_and(image,image,mask = mask) 
#plot the result
plt.imshow(final)


#Edge Detection
"""
Edges are the points in an image where the 
image brightness changes sharply or has discontinuities. 
Such discontinuities generally correspond to:

Discontinuities in depth
Discontinuities in surface orientation
Changes in material properties
Variations in scene illumination
"""
#import the required libraries
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

#read the image
image = cv2.imread('E:\OpenCV\Images\coins.jpg') 
#calculate the edges using Canny edge algorithm
edges = cv2.Canny(image,100,200) 
#plot the edges
plt.imshow(edges)


#Image Filtering

"""
In image filtering, a pixel value is updated using its neighbouring values. 
But how are these values updated in the first place?
Ans: using filters/kernels of size 3x3 or 5x5 etc.
"""


#Face Detection
"""
Face Detection
OpenCV supports haar cascade based object detection. 
Haar cascades are machine learning based classifiers 
that calculate different features like edges, lines, etc in the image. 
Then, these classifiers train using multiple positive and negative samples.

Trained classifiers for different objects like faces,eyes 
etc are available in the OpenCV Github repo , 
you can also train your own haar cascade for any object.
"""

#import required libraries
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# load the classifiers downloaded 
face_cascade = cv.CascadeClassifier('E:\OpenCV\Images\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('E:\OpenCV\Images\haarcascade_eye.xml')
#read the image and convert to grayscale format
img = cv.imread('E:\OpenCV\Images\rotated_face.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#calculate coordinates 
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    #draw bounding boxes around detected features
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#plot the image
plt.imshow(img)
#write image 
cv2.imwrite('E:\OpenCV\Images\face_detection.jpg',img)



##########################################
"""
Face and  Eye Detection on saved Image
"""

import cv2
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# Importing html smaples for Face and Eyes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Reading the given Image and converting it to Grayscale
img = cv2.imread('E:\OpenCV\Images\baby.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting Faces from image using Face_Samples
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Iterating for the dimentions of the Detected faces to draw rectangle
for (x,y,w,h) in faces:
    # Creating Rectangle around Face with color Red and of width 2
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    # Getting start and end points of face to detect eyes within the Face
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    # Detecting Eyes from image using Eye_Samples
    eyes = eye_cascade.detectMultiScale(roi_gray)
    
    # Iterating for the dimentions of the Detected Eyes to draw rectangle
    for (ex,ey,ew,eh) in eyes:
        # Creating Rectangle around Eyes with color Green and of width 2
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img) # Displays the Image with rectangles on Face and Eyes

k = cv2.waitKey(0)
stop = ord("S") # To Stop press capital S (While on the output image)
if k == stop:
    cv2.destroyAllWindows()

elif k == ord('q'):   # To Save and close press q
    cv2.imwrite('marked1.png',img)
    cv2.destroyAllWindows()
    
    
    
    
    
#####################################
"""
Face and Eyes Detection (Live)
"""
import cv2
# https://github.com/opencv/opencv/tree/master/data/haarcascades

# Importing html smaples for Face and Eyes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Starting your Laptop Camera for recording
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()  # Getting image from the camera
    #ret would be 1 if python can read data else 0
    #img is an ndarray, the first image from frames
    """
    print img
    break
    """
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # Converting Image to GrayScale

    # Detecting Faces from image using Face_Samples
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
    # Iterating for the dimentions of the Detected faces to draw rectangle
    for (x,y,w,h) in faces:
        
        # Creating Rectangle around Face with color Red and of width 2
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        
        # Getting start and end points of face to detect eyes within the Face
        roi_gray = gray[y:y+h, x:x+w]  # for GrayScale
        roi_color = img[y:y+h, x:x+w]  # for Coloured
        
        # Detecting Eyes from image using Eye_Samples
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        # Iterating for the dimentions of the Detected Eyes to draw rectangle
        for (ex,ey,ew,eh) in eyes:
            # Creating Rectangle around Eyes with color Green and of width 2
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img) # Displays the Image with rectangles on Face and Eyes
    
    k = cv2.waitKey(30)
    stop = ord("S") # To Stop press capital S (While on the output image)
    if k == stop:
        break

cap.release()
cv2.destroyAllWindows()



#################################
"""
Color Detection (Red, Blue, Green)
"""
import cv2

cap = cv2.VideoCapture(0)

while(1):
    #"Frame" will get the next frame in the camera (via "cap").
    #"ret" will obtain return value from getting the camera frame, either true of false.
    ret,frame = cap.read()
    #we use the function cv2.cvtColor(input_image, flag) where flag determines the type of conversion.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #defining the range of red color
    red_lower = np.array([136,87,111],np.uint8)
    red_upper = np.array([180,255,255],np.uint8)

    #defining the range of blue color
    blue_lower = np.array([99, 115,150],np.uint8)
    blue_upper = np.array([110,255,255],np.uint8)

    #defining the range of yellow color
    yellow_lower = np.array([22,60,200],np.uint8)
    yellow_upper = np.array([60,255,255],np.uint8)

    #finding the range of red, blue and yellow color in the image
    red = cv2.inRange(hsv, red_lower, red_upper)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

    #Morphological transformation, Dilation
    #The kernel slides through the image (as in 2D convolution).
    #A pixel in the original image (either 1 or 0) will be considered 1
    #only if atleast one pixel under the kernel is '1'.
    kernal = np.ones((5,5), "uint8")
    #print kernal

    red = cv2.dilate(red, kernal)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame,mask= red)

    blue = cv2.dilate(blue, kernal)
     # Bitwise-AND mask and original image
    res1 = cv2.bitwise_and(frame,frame,mask= blue)

    yellow = cv2.dilate(yellow, kernal)
     # Bitwise-AND mask and original image
    res2 = cv2.bitwise_and(frame,frame,mask= yellow)

    #Tracking the Red color
    (ret,contours,hierarchy) = cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area>300:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255))


    #Tracking the Blue color
    (ret,contours,hierarchy) = cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area>300:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,"BLUE color",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0))

    #Tracking the Green color
    (ret,contours,hierarchy) = cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area>300:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,"GREEN color",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0))

    cv2.imshow("Color Tracking",frame)
    if cv2.waitKey(10)& 0xff ==ord('S'):
        cap.release()
        cv2.destroyAllWindows()
        break
    

"""
Erosion and dilation are morphological image processing operations. 
Morphological image processing basically deals with modifying geometric structures in the image. 
These operations are primarily defined for binary images, but we can also use them on grayscale images. 
Erosion basically strips out the outermost layer of pixels in a structure, 
where as dilation adds an extra layer of pixels on a structure.
"""











