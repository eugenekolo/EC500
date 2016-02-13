### OpenCV 3.0 + Python 2.7 environment set up on Ubuntu 14.04  
This is a simple tutorial of setting up opencv 3.0 and python 2.7 environment on Ubuntu 14.04 we used for the homework.  
  
#### 1. Pre-install procedure  
##### 1.1 System update  
    $ sudo apt-get update  
    $ sudo apt-get upgrade  
  
##### 1.2 Install basic developer tools  
    $ sudo apt-get install build-essential cmake git pkg-config  
  
##### 1.3 Install basic image I/O packages  
    $ sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev  
  
##### 1.4 Install GTK library  
    $ sudo apt-get install libgtk2.0-dev  
  
##### 1.5 Install video I/O packages  
    $ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev  
  
##### 1.6 Optimization libraries  
    $ sudo apt-get install libatlas-base-dev gfortran  
  
#### 2. Install Python environment  
##### 2.1 Install python packages manager  
    $ wget https://bootstrap.pypa.io/get-pip.py
    $ sudo python get-pip.py  
  
##### 2.2 Install virtual project environment  
    $ sudo pip install virtualenv virtualenvwrapper
    $ sudo rm -rf ~/.cache/pip  
The virtual project environment is not necessary but it will give us great convinence by creating separate Python environments for each project we are working on.  
    
##### 2.3 Edit bashrc file for virtualenv and virtualenvwrapper  
  
Open ~/.bashrc file with gedit and add the follow lines at the end of it, then save it. Thus will ensure both the virtualenv and virtualenvwrapper are properly sourced everytime we log in.(You need to log out and log in again or source ~/.bashrc for this to be effective)    
  
    # virtualenv and virtualenvwrapper
    export WORKON_HOME=$HOME/.virtualenvs  
    source /usr/local/bin/virtualenvwrapper.sh  
  
##### 2.4 Install numpy
  
    $ pip install numpy  
  
#### 3. Install OpenCV  
##### 3.1 Download OpenCV and some other dependent libraries  
  
    $ cd ~
    $ git clone https://github.com/Itseez/opencv.git
    $ cd opencv
    $ git checkout 3.0.0  
  
In order to have the access to some other functions in OpenCV we also need to install the opencv_contrib library:  

    $ cd ~
    $ git clone https://github.com/Itseez/opencv_contrib.git
    $ cd opencv_contrib
    $ git checkout 3.0.0  
  
##### 3.2 Setup the build
  
    $ cd ~/opencv  
    $ mkdir build  
    $ cd build  
    $ cmake -D CMAKE_BUILD_TYPE=RELEASE \  
	    -D CMAKE_INSTALL_PREFIX=/usr/local \  
	    -D INSTALL_C_EXAMPLES=ON \  
	    -D INSTALL_PYTHON_EXAMPLES=ON \  
	    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \  
	    -D BUILD_EXAMPLES=ON ..    
  
##### 3.3 Build the OpenCV
  
    $ make -j4  
    $ sudo make install  
    $ sudo ldconfig  
  
##### 3.4 Create a symbol link for OpenCV and Python  
  
    $ cd ~/.virtualenvs/cv/lib/python2.7/site-packages/  
    $ ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so  
  
##### 3.5 Check the if the environment is successfully installed  
  
    $ workon cv  
    $ python  
    >>> import cv2  
    >>> cv2.__version__  
    
 If everything installed successfully, those input will give out no errors and show the version of OpenCV, which is  
  
    '3.0.0'  
  

      
