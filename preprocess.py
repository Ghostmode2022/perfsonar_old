#!/usr/bin/python
# load text
import re
import sys
print "This is the name of the script: ", sys.argv[1]
fileNameI = sys.argv[1]+'.txt'
fileNameO = sys.argv[1]+'-output.txt'
fileI = open(fileNameI, 'r')
fileO = open(fileNameO, 'w')
textI = []
textI = fileI.read()



#count the number times the word "url" appears
count = textI.count("url")
print 'The number of occurrence of url %s' %count



#split the data and store in an array with the occurrence of url
splitarr = textI.rsplit('url', count)



#get the data between "134.197.11.250/esmond/perfsonar/archive/" and "/","metadata-key":""
for x in range (1, count+1):
  pre = sys.argv[1]+'/esmond/perfsonar/archive/'
  post = '/","metadata-key":"'
  start = splitarr[x].index( pre ) + len( pre )
  end = splitarr[x].index( post, start )
  fileO.write(splitarr[x][start:end])
  fileO.write("\n")



#create as many variable as many as the metadata
  globals()['metadata%s' % x] = splitarr[x][start:end]
#Need to un-comment to see the output
#  print (eval("metadata%s" % (x)))



fileI.close()
fileO.close()
