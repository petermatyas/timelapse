#!/usr/bin/python

import os
import datetime
from datetime import timedelta
import pytz   # pip install pytz
from astral import Astral, GoogleGeocoder   # pip install astral

path = "/media/peti/DC51-49A01/camera"


def night(t):
  hun = pytz.timezone('Europe/Budapest')
  t = datetime.datetime(int(t[0:4]), int(t[4:6]), int(t[6:8]), int(t[8:10]), int(t[10:12]), tzinfo=hun)

  sun = city.sun(date=t, local=True)

  if ((t>sun['sunrise']) & (t<sun['sunset'] + timedelta(minutes = 0))):
    return "day"
  else:
    return "night"

#========================================================================



city_name = 'Szombathely'

a = Astral(GoogleGeocoder)
a.solar_depression = 'civil'     # civil 6, nautical 12, astronomical 18
city = a[city_name]



os.system("ls " + path + "> list.txt") 
f = open('list.txt','r')
for line in f:
    line = line.rstrip('\n')
    if line[0]=="2":     
      if (night(line) == "night"):
        os.system("mv " + path + "/" + line + " " + path + "/night/" + line)
        print ("%s night %s:%s" %(line, line[8:10], line[10:12]))
      else:
        print ("%s day   %s:%s" %(line, line[8:10], line[10:12]))

f.close()
os.system("rm list.txt") 

