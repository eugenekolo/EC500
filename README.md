EC500 Group 2: Utilize OpenCV for human face detection

※Overview

In this mini-project we used OpenCV to implement human face detection, and programming language is python. There are tons of mature implementations for this topic you can either choose to train your own algorithm with OpenCV or grab a trained detector in to practise. Here we specifcically looked into a built-in feature named Haar-cascade detection.

※Algorithm

Haar feature-based cascade is a widely-used and mature object detectioin algorithm. OpenCV has these built-in classifiers(e.g. cv2.CascadeClassifier()). It is based on such features as eye being darker than nose/cheek areas and the bridge of our nose. OpenCV has also sorted out certain features to optimize the performance by training it with image database. You can find details of this algorithm in OpenCV tutorial page here:

http://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html#gsc.tab=0

※Code

The code we used is simple and elegant. 
Load the xml files and run the code. 
*python face_detect.py abba.png haarcascade_frontalface_default.xml*
Code credit:Shantnu Tiwari. If you want to understand how the code works, the details are here:

https://realpython.com/blog/python/face-recognition-with-python/

※Feed the program with different images

Photo Credit:

※Find the right threshold

scaleFactor
minNeighbors
minSize

Here are some useful points we find:
Parameters:

scaleFactor: Since some faces may be closer to the camera, they would appear bigger than those faces in the back. The scale factor compensates for this
if scaleFactor is too small, it reads false faces; too big it misses some faces

minNeighbors:how many objects are detected near the current one before it declares the face found
small minNeighbors helps detecting some small faces in crawed pics, but also gives some false readings(repeat detection), reduce saceFactor seems fix that

minSize: gives the size of each window 
if faces are too small compared to the whole picture, miniSize has to be set small, ie: carmeet

tunning steps: determine minisize -> miniNeighbors -> scaleFactor -> miniNeighbors

※Discrepencies

※Additional comments

