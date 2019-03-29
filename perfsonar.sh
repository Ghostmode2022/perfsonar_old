#!/bin/bash
ip=134.197.11.250
echo -e "\n Executing the first curl query to get the alphaneumeric value \n"
curl http://$ip/esmond/perfsonar/archive/ >> /home/sid/perfsonar/$ip.txt
echo -e "\n Create the output file\n"
touch /home/sid/perfsonar/$ip-output.txt
echo -e "\n Executing the python file to extract the alphaneumeric value \n"
chmod 777 preprocess.py
./preprocess.py $ip
