#!/bin/bash

sudo apt-get update  
sudo apt-get upgrade  

# OpenCV C stuff
sudo apt-get install build-essential cmake git
sudo apt-get install libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libatlas-base-dev gfortran 

git clone https://github.com/Itseez/opencv
git clone https://github.com/Itseez/opencv_contrib.git
cd opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib ..
make -j4
sudo make install

# OpenCV python bindings
mkvirtualenv cv
sudo apt-get install python2.7-dev
sudo pip2 install numpy
sudo pip2 install pillow
ln -s /usr/local/lib/python2.7/site-packages/cv2.so ~/.virtualenvs/cv/lib/python2.7/site-packages/cv2.so
