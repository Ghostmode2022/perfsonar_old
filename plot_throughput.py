#!/usr/bin/python
#python plot_throughput.py 206.207.50.6 throughput ae7b607a924f4af8b3f8f979c70f95f1 

#First argument is the ip address
#Second argument is the event-type
#Third argument is the metadata

import numpy as np
import sys
import matplotlib.pyplot as plt
import time
from datetime import datetime

fileNameI = '/home/sid/perfsonar/data/'+sys.argv[1]+'/'+sys.argv[2]+'/'+sys.argv[1]+'-'+sys.argv[3]+'-'+sys.argv[2]+'.txt'
fileNameO = '/home/sid/perfsonar/data/'+sys.argv[1]+'/'+sys.argv[2]+'/'+sys.argv[1]+'-'+sys.argv[3]+'-'+sys.argv[2]+'-output.txt'
fileI = open(fileNameI, 'r')
#textI = []
textI = fileI.read()
# Replace the target string
textO1 = textI.replace(',"val":', '	')
textO2 = textO1.replace('{"ts":', '')
textO3 = textO2.replace('[', '')
textO4 = textO3.replace(']', '')
textO5 = textO4.replace('},', "\n")
textO = textO5.replace('}', '')
textO = textO.split('\n')

x = [row.split('	')[0] for row in textO]
for i in range (len(x)):
  a = x[i]
  b = int(a)
  c = datetime.utcfromtimestamp(b).strftime("%m:%d:%Y-%H:%M:%S")
  x[i] = c
y = [row.split('	')[1] for row in textO]

fig = plt.figure()

ax1 = fig.add_subplot(111)



ax1.set_title("Throughput timeseries graph")    
ax1.set_xlabel('time-stamp')
ax1.set_ylabel('throughput')
#c='r',
ax1.plot(x,y, 'ro', label= sys.argv[3])

#first argument is the lowest value, second argument is the max value and 
plt.xticks(np.arange(0, 50, 10))
plt.yticks(np.arange(0, 50, 10))

#ax1.pyplot.locator_params(axis='y', nbins=6)
#ax1.pyplot.locator_params(axis='x', nbins=10)



leg = ax1.legend()

plt.show()
