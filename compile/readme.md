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



# Compile OpenCV with VIDEO feature for Ubuntu
https://github.com/menpo/conda-opencv

$ git clone https://github.com/conda-recipes
$ cd conda-recipes

* if ffmpeg isn't insatlled , 'conda install ffmpeg'
* if libgtk2.0-dev pkg-condig aren't installed, install them.
	* $ sudo apt update
	* $ sudo apt install libgtk2.0-dev pkg-config

* modify meta.yaml
	* comment out 'patches' section
	* modify ffmpeg version 2.8 -> x.x
* modify build.sh
	* -DWITH_GTK=1
	* -DWITH_FFMPEG=1

$ conda build opencv

* check build log
> --   OpenCV modules:
> --     To be built:                 core flann hdf imgproc ml photo reg surface_matching video dnn fuzzy imgcodecs shape videoio highgui objdetect plot superres xobjdetect xphoto bgsegm bioinspired dpm face features2d line_descriptor saliency text calib3d ccalib datasets rgbd stereo tracking videostab xfeatures2d ximgproc aruco optflow phase_unwrapping stitching structured_light python3
> --   GUI: 
> --     GTK+ 2.x:                    YES (ver 2.24.30)
> --     GThread :                    YES (ver 2.48.2)

$ conda install opencv=3.2.0 --use-local

* check install

$ conda list
> opencv                    3.2.0               np111py36_0    local


## trouble shoot 

* zipfile.BadZipFile: File is not a zip file
environment location: /home/suzuki/anaconda3/conda-bld/opencv_1520032161283/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_plac
 -> reinstall anaconda -> not solve


