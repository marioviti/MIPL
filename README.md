# MIPL
My Image Processing Library

# What is MIPL 
A collection of image processing routines from opencv, numpy and scipy.

* python version: 3.5.2
* opencv verison: 3.2.0
* numpy version: 1.13.0
* scipy version: 0.19.0

# How to setup a virtualenv

The main reference [tutorial](http://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/)

Set of instructions:

```
python3 -venv cv;
source cv/bin/activate;
pip install numpy;
pip install scipy;
mkdir cv/src;
cd cv/src;
git clone https://github.com/Itseez/opencv.git;
cd opencv;
git checkout 3.2.0;
cd ..;
git clone https://github.com/Itseez/opencv_contrib.git;
cd opencv_contrib
git checkout 3.2.0;
cd ../opencv;
mkdir build;
cd build;
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules .. ;
make -j<num of threads>;
make install;
cd cv/lib/python3.5/site-packages/;
ln -s /usr/local/lib/python3.5/site-packages/cv2.cpython-34m.so cv2.so;
```
