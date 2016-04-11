#!/bin/bash

# based on: https://bbs.archlinux.org/viewtopic.php?id=191398

h=`date +%H`

morning=4
evening=21

m="/media/usbdrive"
#m="/media/peti/DC51-49A0"  # kingston 16 GB
#m="/media/pi/726E-8C9E"  # 4 GB

cm=$(mountpoint $m)				# cm = check mountpoint
mr="/media/usbdrive is a mountpoint"		# mr = mounted result
cup=$(lsblk | grep "sd[a-z]1")			# cup = check usb is plugged in
er=""						# er = empty result

DATE=$(date +"%Y%m%d%H%M%S")
spaceroot=$(df -m / | tail -1 | awk '{print $4}')	# free space in root in MB
spaceusb=$(df -m | grep /dev/s | awk '{print $4}')	# free space in USB in MB
A=$(ls /dev/s[a-z][a-z][0-9])

if [ "$cup" != "$er" ]; then		# USB is plugged
  echo "usb is plugged"
  if [ "$cm" != "$mr" ]; then 		# USB mounted?
    echo "usb is not mounted"
    sudo mount $A /media/usbdrive -o uid=pi,gid=pi
    echo "mounting point:"
    echo $A
    if [ ! -d $m/camera ]; then
      mkdir -p $m/camera
    fi
  fi

  if [ $spaceroot -gt 10 ]; then
    echo "van hely a root-on"
    if [ ! -d /media/usbdrive/camera ]; then
      mkdir -p /media/usbdrive/camera
    fi
    if [ $h -lt $morning ] && [ $h -ge $evening ] && [$n -eq "no"];  then
      echo "night"
    else
      echo "picture save to USB drive"
      raspistill -t 2000 -rot 180 -o $m/camera/$DATE.png -e png  
    fi
    
  else
    echo "nincs hely a root-on"
    if [ $spaceusb -gt 10 ]; then
      echo "van hely a pendrive-n"
      echo "picture save to RPi"
      if [ ! -d /home/pi/camera ]; then
    	mkdir -p /home/pi/camera
      fi
      if [ $h -lt $morning ] && [ $h -ge $evening ] && [$n -eq "no"];  then
        echo "night"
      else
        echo "picture save to RPi"
        raspistill -t 2000 -rot 180 -o /home/pi/camera/$DATE.png -e png
      fi
    else
      echo "nincs hely a pendrive-n"
    fi
  fi
  else 
  echo "usb is not mounted" 
  if [ ! -d /home/pi/camera ]; then
    mkdir -p /home/pi/camera
  fi
  if [ $h -lt $morning ] && [ $h -ge $evening ] && [$n -eq "no"]; then
    echo "night"
  else
    echo "picture save to RPi"
    raspistill -t 2000 -rot 180 -o /home/pi/camera/$DATE.png -e png
  fi
fi
