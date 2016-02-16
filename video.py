#!/usr/bin/python

import os
import time
import getpass

#=== Config ==============================================================================================
framerate  = "15"
startDay   = "20160128"
stopDay    = "20160128"
textSize   = "120"		# default: 120

pathToPictures = "/media/" + getpass.getuser() + "/KA/camera"	# external hard drive contain the pictures
#workingFolder = os.getcwd()
workingFolder = "/home/peti/timelapseWork"
#=== Config end ==========================================================================================


#=== Create lists =====================================
os.system("ls " + pathToPictures + " > " + workingFolder + "/list_.txt")	# create file list
f3 = open(workingFolder + '/list_.txt','r')    					# temporary / all files
f = open(workingFolder + '/list.txt','w')      					# all pictures
f2 = open(workingFolder + '/list2.txt','w')    					# days

lineArchive = " " 

for line in f3:
  line = line.rstrip('\n')
  if line[0]=="2":
    f.write(line + "\n")
    if ((lineArchive != line[0:8]) and (int(line[0:8]) >= int(startDay)) and (int(line[0:8]) <= int(stopDay)) and not(os.path.isfile(workingFolder + "/" + line[0:8] + "_" + framerate + "fps.mp4"))):
      f2.write(line[0:8] + "\n") 
      lineArchive = line[0:8]   

f3.close()
f2.close()
f.close()

os.system("rm " + workingFolder + "/list_.txt")

#=== Select pictures and convert video ================
f2 = open(workingFolder + '/list2.txt','r')

i = 0
for line2 in f2:
  f = open(workingFolder + '/list.txt','r')
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
    text = year + "/" + month + "/" + day 
    if ((year == year2) and (month == month2) and (day == day2)):
    # copy to working folder
      os.system("cp " + pathToPictures + "/" + line + " " + workingFolder)      
    # labelling
      os.system("convert " + workingFolder + "/" + line + " -pointsize " + textSize + " -fill white -gravity southeast -annotate +100+100 " + text + " " + workingFolder + "/0" + line)
    # resize and crop picture:
      os.system("convert " + workingFolder + "/0" + line + " -gravity south -crop 2592x1458+0+0 " + workingFolder + "/" + line)
    # remove the temp pictures:	
      os.system("rm " + workingFolder + "/0" + line)
  # convert video
  os.system("ffmpeg -r " + framerate + " -i " + workingFolder + "/%*.png " + " -s hd1080 -vcodec libx264 " + workingFolder + "/" + line2 + "_" + framerate + "fps.mp4")
  # clear pictures
  os.system("rm " + workingFolder + "/*.png")
  f.close()
f2.close()

#=== Merge videos =====================================
print "merge videos"
os.system("ls " + workingFolder + " | grep mp4 > videolist0.txt")
f3 = open(workingFolder + '/videolist.txt','w')  
f4 = open('videolist0.txt','r') 
for line in f4:
  if (line[9:11] == framerate) and (int(line[0:8]) >= int(startDay)):
    f3.write("file " + line)
f4.close()
f3.close()
os.system("ffmpeg -f concat -i " + workingFolder + "/videolist.txt -codec copy output_" + framerate + "fps.mp4")


#== Clean =============================================
os.system("rm " + workingFolder + "/list.txt")
os.system("rm " + workingFolder + "/list2.txt")
os.system("rm videolist0.txt")
os.system("rm " + workingFolder + "/videolist.txt")
