#!/usr/bin/python
# load text
import re
import sys
import time
from subprocess import Popen
import geocoder
from math import sin, cos, sqrt, atan2, radians
#Defining the value of radian
R = 6373.0
source = sys.argv[1]
#get the latitude and longitude of the source
#need to convert the ip address into radians by lat1 = radians(37.751)
#lon1 = radians(-97.822)
#lat2 = radians(40.4259)
#lon2 = radians(-86.9081)
g = geocoder.ip(source)
source_lat1 = g.lat
source_long1 = g.lng
source_lat = radians(source_lat1)
source_long = radians(source_long1)

#metadata = sys.argv[2]
fileNameI = '/home/sid/perfsonar/'+sys.argv[1]+'-'+sys.argv[2]+'-packet-trace'+'.txt'
fileNameO = '/home/sid/perfsonar/sid-output.txt'
fileNameO1 = '/home/sid/perfsonar/sid.txt'
fileNameO2 = '/home/sid/perfsonar/sid2.txt'
fileI = open(fileNameI, 'r')
fileO = open(fileNameO, 'w')
fileO1 = open(fileNameO1, 'w')
fileO2 = open(fileNameO2, 'w')
textI = []
textI = fileI.read()

count = textI.count("ts")
#split the data and store in an array with the occurrence of url
#splitarr = textI.rsplit('ts', count)
splitarr = textI.split('ts')

#get the data between "134.197.11.250/esmond/perfsonar/archive/" and "/","metadata-key":""
for x in range (1, count+1):
  result = re.search('":(.*),"val":', splitarr[x])
  fileO.write(result.group(1))
  fileO.write("\t")

#convert the unix timestamp into human readable format
  date = time.ctime(int(result.group(1)))
  fileO.write(date)
  fileO.write("\t")

  fileO.write(source)
  fileO.write("\t")
  

#write the destination ip address in the file 
  result1 = re.search('"ip":"(.*)","', splitarr[x])
  destination = result1.group(1).split('"')[0]
  fileO.write(destination)
  fileO.write("\t")

#get the latitude and longitude of the destination ip address
  g = geocoder.ip(destination)
  dest_lat1 = g.lat
  dest_long1 = g.lng
  dest_lat = radians(dest_lat1)
  dest_long = radians(dest_long1)
  
#get the distance between source and destination
  lat_diff = dest_lat - source_lat
  long_diff = dest_long - source_long
  a = sin(lat_diff / 2)**2 + cos(source_lat) * cos(dest_lat) * sin(long_diff / 2)**2
  c = 2 * atan2(sqrt(a), sqrt(1 - a))
  distance = R * c
  fileO.write(str(distance) + " km")
  fileO.write("\t")

#for x in range (1, count+1):  
  result2 = re.search('"rtt":(.*),"', splitarr[x])
  fileO.write(result2.group(1).split(',')[0])
  fileO.write("\n")

fileI.close()
fileO.close()
fileO1.close()
fileO2.close()
