#!/bin/bash

if [ ! -d /home/pi/camera ]; then
    mkdir -p /home/pi/camera
fi




DATE=$(date +"%Y%m%d%H%M%S")

raspistill -t 2000 -rot 180 -o /home/pi/camera/$DATE.png -e png
