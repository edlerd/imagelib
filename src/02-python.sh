#!/bin/bash

# load virtualenvwrapper for python (after custom PATHs)
venvwrap="virtualenvwrapper.sh"
/usr/bin/which $venvwrap
if [ $? -eq 0 ]; then
    venvwrap=`/usr/bin/which $venvwrap`
    source $venvwrap
fi


workon OpenCV-3.4.3-py3
cd /root/src
ipython -i imageload.py
