#!/bin/bash

# WARNING
# Line 12 erases current docker containers and 
# generates new ones.

containersToGenereate=1000
writeToFile='unique_names.txt'

touch $writeToFile

sudo docker rm $(sudo docker ps -aq)

i=0
while [ $i -lt $containersToGenereate ]
do
    echo $i
    sudo docker run -d hello-world
    i=`expr $i + 1`
done

sleep 1

sudo docker ps -a | awk '{print $12}' > $writeToFile
cat $writeToFile
#sudo docker ps -a