#!/bin/sh

ls -l /dev/disk/by-uuid
echo "-------------------------"
echo "csatolasi pont:"
read A
sudo mount /dev/$A /media/usbdrive -o uid=pi,gid=pi
echo "kesz"
