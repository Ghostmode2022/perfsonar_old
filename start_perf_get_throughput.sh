#!/bin/bash
ip=$1
echo -e "\n Executing the first curl query to get the alphaneumeric value \n"
curl http://$ip/esmond/perfsonar/archive/ >> /home/sid/perfsonar/$ip.txt
echo -e "\n Create the output file\n"
touch /home/sid/perfsonar/$ip-output.txt
#touch command is used to create a file without any content
echo -e "\n Executing the python file to extract the metadata \n"
chmod 777 preprocess.py
#./preprocess.py $ip
