#!/bin/bash

# load image from web
#docker pull spmallick/opencv-docker:opencv

# allow opening graphics on host machine
xhost +local:docker

# start ipython in container
docker run --volume ~/dev/cv/src:/root/src --device=/dev/video0:/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -p 5000:5000 -p 8888:8888 -it spmallick/opencv-docker:opencv /root/src/02-python.sh
