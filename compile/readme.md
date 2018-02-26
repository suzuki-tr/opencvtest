# OpenCV

## reference

* (latest doc)[https://docs.opencv.org/master/index.html]
* (other version)[https://docs.opencv.org/]
* (github)[https://github.com/opencv/opencv]
* (releases)[https://opencv.org/releases.html]


## archive of various versions
* wget https://github.com/opencv/opencv/archive/{{ version }}.zip

## environment
* conda install numpy

## How to compile with specific function

* cd opencv-3.0.0
* mkdir build
* cd build
* cmake -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_SHARED_LIBS=NO -D BUILD_opencv_python2=ON -D CMAKE_INSTALL_PREFIX=<PATH OF RELEASE> ..
* make
* make install

## sample cmake command

* minimum
	* cmake -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_SHARED_LIBS=NO -D BUILD_opencv_python2=ON -D BUILD_opencv_python3=ON -D BUILD_opencv_ml=OFF -D BUILD_opencv_flann=OFF -D BUILD_opencv_features2d=OFF -D BUILD_opencv_photo=OFF -D BUILD_opencv_objdetect=OFF -D BUILD_opencv_video=OFF -D BUILD_opencv_videoio=OFF -D BUILD_opencv_ts=OFF -D BUILD_opencv_calib3d=OFF -D CMAKE_INSTALL_PREFIX=/home/suzuki/opencv/3.0 ..

* with features2D
	* cmake -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_SHARED_LIBS=NO -D BUILD_opencv_python2=ON -D BUILD_opencv_python3=ON -D BUILD_opencv_ml=ON -D BUILD_opencv_flann=ON -D BUILD_opencv_features2d=ON -D BUILD_opencv_photo=OFF -D BUILD_opencv_objdetect=OFF -D BUILD_opencv_video=OFF -D BUILD_opencv_videoio=OFF -D BUILD_opencv_ts=OFF -D BUILD_opencv_calib3d=OFF -D CMAKE_INSTALL_PREFIX=/home/suzuki/opencv/3.0 ..


## dependencies os functions

* calib3d (deps: hal core flann imgproc ml imgcodecs videoio highgui features2d)
* core (deps: hal)
* features2d (deps: hal core flann imgproc ml imgcodecs videoio highgui)
* flann(deps: hal core)
* highgui(deps: hal core imgproc imgcodecs videoio)
* imgcodecs(deps: hal core imgproc)
* ml(deps: hal core)
* objdetect(deps: hal core imgproc ml imgcodecs videoio highgui)
* python3 shape(deps: hal core imgproc video)
* stitching(deps: hal core flann imgproc ml imgcodecs videoio highgui objdetect features2d calib3d)
* superres(deps: hal core imgproc video imgcodecs videoio)
* ts(deps: hal core imgproc imgcodecs videoio highgui)
* video(deps: hal core imgproc)
* videoio(deps: hal core imgproc imgcodecs)
* videostab
* 3.4
	* python2 -> python_bindings_generator

## trouble shoot

* cannot create so file
	* コンパイルオプション BUILD_opencv_python2=ON を指定しているのに、ビルドログのUnavailableに python2、python3が挙がっている。
	* Could NOT find PythonLibs (missing:  PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS) 
	* change python version
		* conda uninsatll python
		* conda install python=2.7


