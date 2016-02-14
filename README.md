EC500 Group 2: Utilize OpenCV for human face detection (and recognition)

##※ Overview
In this mini-project we used [OpenCV](http://opencv.org/) to implement human face detection, and recognition. Programming was done in python, using the OpenCV python bindings. 

### Requirements

-  Utilize OpenCV for 2 human face detection algorithms
	- [x] Harr Cascade Face Detector
	- [x] Eigenfaces Face Recognizer
- Test on the AT&T face set
       - [x] Results for Harr Cascade
       - [x] Results for Eigenfaces
- Deliver:
      - [x] Test Set
      - [x] Training Set
      - [x] Software on Github
      - [x] Executable on Linux platform

##※ Face detection
Haar feature-based cascade is a widely-used and mature object detectioin algorithm. OpenCV has these built-in classifiers(e.g. cv2.CascadeClassifier()). It is based on such features as eye being darker than nose/cheek areas and the bridge of our nose. OpenCV has also sorted out certain features to optimize the performance by training it with image database. You can find details of this algorithm in OpenCV tutorial page here:

http://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html#gsc.tab=0

### Code
The code we used is simple and elegant. 
Load the xml files and run the code. 
*python face_detect.py abba.png haarcascade_frontalface_default.xml*
Code credit:Shantnu Tiwari. If you want to understand how the code works, the details are here:

https://realpython.com/blog/python/face-recognition-with-python/

### Parameters
We performed testing with different parameters to our Harr Cascade Face Detector.

Useful parameters:

* **scaleFactor**: Compenstates for the relative size of faces due to the distance to the focal point (e.g. camera).  Increasing the scaleFactor increases the expected size of a person's face, and decreasing decreases teh expected size of a person's face.

* **minNeighbors**: The number of objects that must be detected near the current one, before the face is declared found. A low **minNeighbors** helps to detect small faces in crowded places, but also increases the number of false positives.

* **minSize**: The minimum size of each face window (e.g. the square). If faces are too small compared to the whole picture, **minSize** has to bet smaller. 

We found tuning in this order to be the easiest to get the right results:  
**minSize** -> **minNeighbors** -> **scaleFactor** -> **minNeighbors**


### Results

##※ Face recognition
TODO

### Code
 TODO

### Usage
TODO

### Results
