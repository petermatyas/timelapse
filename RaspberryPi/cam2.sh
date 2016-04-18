#!/bin/bash

# auto mount source: https://bbs.archlinux.org/viewtopic.php?id=191398

h=`date +%H`

m="/media/usbdrive"
#m="/media/peti/DC51-49A0"  # kingston 16 GB
#m="/media/pi/726E-8C9E"  # 4 GB

cm=$(mountpoint $m)                             # cm = check mountpoint
mr="/media/usbdrive is a mountpoint"    # mr = mounted result
cup=$(lsblk | grep "sd[a-z]1")                  # cup = check usb is plugged in
er=""                                           # er = empty result

DATE=$(date +"%Y%m%d%H%M%S")
spaceroot=$(df -m / | tail -1 | awk '{print $4}')
spaceusb=$(df -m | grep /dev/s | awk '{print $4}')
A=$(ls /dev/s[a-z][a-z][0-9])
if [ "$cup" != "$er" ] 
  then
  echo "usb bedugva"
  if [ "$cm" = "$mr" ]
    then 
    echo "usb nincs mountolva"
    sudo mount $A /media/usbdrive -o uid=pi,gid=pi
    echo "mounting point:"
    echo $A
    if [ ! -d $m/camera ]; then
      mkdir -p $m/camera
    fi
  fi
  else 
  echo "usb nincs bedugva"
fi

# camera directory check
if [ ! -d /home/pi/camera ]; then
    mkdir -p /home/pi/camera
fi


if [ "$cm" = "$mr" ]; 
  then
 
  echo "pendrive bedugva, mountolva"
  if [ $spaceroot -gt 10 ] 
    then
    echo "van hely a root-on"
    echo "picture save to USB drive"
    if [ $h -ge 4 ] && [ $h -lt 21 ]; 
      then
      raspistill -t 2000 -rot 180 -o $m/camera/$DATE.png -e png
      else
      echo "night"
    fi
    
    else
    echo "nincs hely a root-on"
      if [ $spaceusb -gt 10 ]
        then
        echo "van hely a pendrive-n"
        echo "picture save to RPi"
        if [ $h -ge 4 ] && [ $h -lt 21 ]; 
          then
          raspistill -t 2000 -rot 180 -o /home/pi/camera/$DATE.png -e png
          else
          echo "night"
        fi
        else
        echo "nincs hely a pendrive-n"
      fi
  fi
  else
  echo "pendrive nincs bedugva"
  echo "picture save to RPi"
  if [ $h -ge 4 ] && [ $h -lt 21 ]; 
    then
    raspistill -t 2000 -rot 180 -o /home/pi/camera/$DATE.png -e png
    else
    echo "night"
  fi
fi
  



