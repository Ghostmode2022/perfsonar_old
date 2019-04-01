#!/bin/bash
ip="$1"
fileI="$1-output.txt"
while IFS= read -r metadata
do
  touch /home/sid/perfsonar/$ip-throughput.txt
  curl "http://$ip/esmond/perfsonar/archive/$metadata/throughput/base?" >> /home/sid/perfsonar/$ip-throughput.txt
done < "$fileI"
