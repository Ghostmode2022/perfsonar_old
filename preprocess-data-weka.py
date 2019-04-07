#!/usr/bin/python
#192.148.201.132-b3d810cf4b6247be835392de328b32db-packet-loss-rate
import re
import sys
import sys, os
import subprocess
print "The ip address is: ", sys.argv[1]
print "The metadata is: ", sys.argv[2]
print "The event type is: ", sys.argv[3]
var1 = sys.argv[1]
var2 = sys.argv[2]
var3 = sys.argv[3]
print var1
print var2
print var3
fileNameI = ''sys.argv[1]+'-'+sys.argv[2]+'-'+sys.argv[3]+'.txt'
fileNameO = sys.argv[1]+'-'+sys.argv[2]+'-'+sys.argv[3]+'-output.txt'
fileI = open(fileNameI, 'r')
fileO = open(fileNameO, 'w+')
textI = []
textI = fileI.read()
#calculating the number of datapoints
count = textI.count("ts")
print 'The number of datapoints present in the current file is %s' %count
#Replace '[' with null
textI = textI[1:-1]
textI = textI[1:-1]
#preparing the file to be weka recognisable format
fileO.write('@predict\n')
fileO.write('@attribute timestamp neumeric\n')
fileO.write('@attribute value neumeric\n')
fileO.write('@data\n\n')
textI1 = textI.replace('},{', '\n')
textI2 = textI1.replace('"ts":', '')
textI3 = textI2.replace(',"val":', '\t')
fileO.write(textI3)
fileO.close()
fileI.close()
#rename the file to convert into weka recognisable format 
os.rename(sys.argv[1]+'-'+sys.argv[2]+'-'+sys.argv[3]+'-output.txt', sys.argv[1]+'-'+sys.argv[2]+'-'+sys.argv[3]+'-output.arff')
