#!/bin/bash

h=`date +%H`

if [ ! -d /home/pi/camera ]; then
    mkdir -p /home/pi/camera
fi

if [ $h -ge 4 ] && [ $h -lt 21 ]; then
  DATE=$(date +"%Y%m%d%H%M%S")
  raspistill -t 2000 -rot 180 -o /home/pi/camera/$DATE.png -e png
fi



