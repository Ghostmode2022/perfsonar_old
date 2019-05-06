#!/usr/bin/python
import re
import sys
import sys, os
import subprocess
#First argument is the ip address
#Second argument is the event-type
#Third argument is the metadata
###################print "This is the name of the script: ", sys.argv[1]
###################var1 = sys.argv[1]
###################var2 = sys.argv[2]
###################var3 = sys.argv[3]
fileNameI = '/home/sid/perfsonar/data/'+sys.argv[1]+'/'+sys.argv[2]+'/'+sys.argv[1]+'-'+sys.argv[3]+'-'sys.argv[2]'.txt'
fileI = open(fileNameI, 'r')
textI = []
textI = fileI.read()
print textI[1]
#python plot_throughput 206.207.50.6 throughput ae7b607a924f4af8b3f8f979c70f95f1 
