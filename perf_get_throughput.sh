#!/bin/bash
ip="$1"
fileI="/home/sid/perfsonar/data/$1/$1-output.txt" #need to include the data directory
while IFS= read -r metadata
do
  #Querying Throughput
  mkdir /home/sid/perfsonar/data/$ip/throughput
  touch /home/sid/perfsonar/data/$ip/throughput/$ip-throughput.txt
  curl "http://$ip/esmond/perfsonar/archive/$metadata/throughput/base?" >> /home/sid/perfsonar/data/$ip/throughput/$ip-$metadata-throughput.txt
  python /home/sid/perfsonar/process-data-weka.py $ip $metadata throughput
  
  #Querying Packet Loss
  mkdir/home/sid/perfsonar/data/$ip/packet-loss
  touch /home/sid/perfsonar/data/$ip/packet-loss/$ip-packet-loss-rate.txt
  curl "http://$ip/esmond/perfsonar/archive/$metadata/packet-loss-rate/base" >> /home/sid/perfsonar/data/$ip/packet-loss/$ip-$metadata-packet-loss-rate.txt
  python /home/sid/perfsonar/process-data-weka.py $ip $metadata packet-loss

  #Querying Packet Traces
  mkdir /home/sid/perfsonar/data/$ip/packet-traces
  touch /home/sid/perfsonar/data/$ip/packet-traces/$ip-packet-trace.txt  
  curl "http://$ip/esmond/perfsonar/archive/$metadata/packet-trace/base?time-range=600" >> /home/sid/perfsonar/data/$ip/packet-traces/$ip-$metadata-packet-trace.txt
  python /home/sid/perfsonar/process-data-weka.py $ip $metadata packet-traces

  #Querying Subinterval Data
  mkdir /home/sid/perfsonar/data/$ip/subinterval-data
  touch /home/sid/perfsonar/data/$ip/subinterval-data/$ip-subinterval-data.txt
  curl "http://$ip/esmond/perfsonar/archive/$metadata/packet-retransmits-subintervals/base?time-range=86400" >> /home/sid/perfsonar/data/$ip/subinterval-data/$ip-subinterval-data.txt
  python /home/sid/perfsonar/process-data-weka.py $ip $metadata subinterval-data
done < "$fileI"
