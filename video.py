#!/usr/bin/python

import os
import time
import getpass

#=== Config ==============================================================================================
framerate  = "24"
startDay   = "20160213"
stopDay    = "20190210"
mergeVideo = "yes"		# yes|no	default: yes
resolution = "1280x720"
textSize   = "120"

pathToPictures = "/media/" + getpass.getuser() + "/KA/camera"	# external hard drive contain the pictures
#workingFolder = os.getcwd()
workingFolder = "/home/arpad/timelapse"
#=== Config end ==========================================================================================


#=== Create log =======================================
log = open(workingFolder + 'log.txt','a')

#=== Create lists =====================================
os.system("ls " + pathToPictures + " > " + workingFolder + "/list_.txt")	# create file list
f3 = open(workingFolder + '/list_.txt','r')    					# temporary / all files
f = open(workingFolder + '/list.txt','w')      					# all pictures
f2 = open(workingFolder + '/list2.txt','w')    					# days

lineArchive = " " 
pic = 0
day = 0

for line in f3:
  line = line.rstrip('\n')
  pic = pic + 1
  if line[0]=="2":
    f.write(line + "\n")
    if (lineArchive != line[0:8]) and (int(line[0:8]) >= int(startDay) and (int(line[0:8]) < stopDay) and not (os.path.isfile(line[0:8] + "_" + framerate + "fps.mp4"))):
      day = day + 1
      f2.write(line[0:8] + "\n") 
      lineArchive = line[0:8]   

f3.close()
f2.close()
f.close()

os.system("rm " + workingFolder + "/list_.txt")
log.write("number of pictures: " + str(pic) + "\n")
log.write("number of days:     " + str(day) + "\n")

#=== Select pictures and convert video ================
f2 = open(workingFolder + 'list2.txt','r')

i = 0
for line2 in f2:
  f = open('list.txt','r')
  line2 = line2.rstrip('\n')
  print "copy files: " + line2
  year2 = line2[0:4]
  month2 = line2[4:6]
  day2 = line2[6:8]
  i = i + 1
  for line in f:
    line = line.rstrip('\n')
    year = line[0:4]
    month = line[4:6]
    day = line[6:8]       
    if ((year == year2) and (month == month2) and (day == day2)):
      os.system("cp " + pathToPictures + "/" + line + " " + workingFolder)      
    # copy to working folder
    # label
      text = year + "/" + month + "/" + day                                     
    # format of label, resize and crop picture:
      os.system("convert " + line + " -resize 1280x960 -gravity South -crop 1280x720+0+0 -pointsize " + textSize + " -fill white -gravity southeast -annotate +150+100 " + text + " -append " + workingFolder + "/0" + line)	
    # remove the picture without label:
      os.system("rm " + workingFolder + "/" + line)	
  print "convert files: " + line2
  os.system("ffmpeg -r " + framerate + " -i *.png -s " + "1280x960" + " -vcodec libx264 " + workingFolder + "/" + line2 + "_" + framerate + "fps.mp4")					# convert video
  os.system("rm *.png")
  f.close()

f2.close()

print("kepek szama: %d" %i)

#=== Merge videos =====================================
if (mergeVideo == "yes"):
  print "merge videos"
  os.system("ls | grep mp4 > videolist0.txt")
  f3 = open('videolist.txt','w')  
  f4 = open('videolist0.txt','r') 
  for line in f4:
    if (line[9:11] == framerate) and (int(line[0:8]) >= int(startDay)):
      f3.write("file " + line)
  f4.close()
  f3.close()
  os.system("ffmpeg -f concat -i videolist.txt -codec copy output_" + framerate + ".mp4")


#== Clean =============================================
os.system("rm " + workingFolder + "/list.txt")
os.system("rm " + workingFolder + "/list2.txt")
os.system("rm " + workingFolder + "/videolist0.txt")
log.close()
