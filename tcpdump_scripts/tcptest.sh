#!/bin/bash

INPUT1=out.csv
OUTPUT1=out2.txt
count=0

for i in $(cat $INPUT1)
do
temp=$i
length=$(echo $i | awk -F',' '{print $2}')

temp1=$(echo $i | grep -o -e "[0-9][0-9]:[0-9][0-9]:[0-9][0-9]\.[0-9][0-9][0-9][0-9][0-9][0-9]" )  
#It is taking upto 4 dp of the second field

hours=$(echo "$temp1" | awk -F':' '{print $1}')
minutes=$(echo "$temp1" | awk -F':' '{print $2}')
seconds=$(echo "$temp1" | awk -F':' '{print $3}')

#echo "$seconds" 

hourinsec=$(echo "$hours * 36000000" | bc)
mininsec=$(echo "$minutes * 600000" | bc)
secin4dp=$(echo "$seconds * 10000" | bc)

time2=$(echo "$hourinsec + $mininsec + $secin4dp" | bc)

#echo "$time2"

if [ $count -eq 0 ]
then
time1=$(echo "$hourinsec + $mininsec + $secin4dp" | bc)
count=$(($count + 1))
lengthprev=$length

else
timediff=$(echo "$time2 - $time1" | bc)
echo "$timediff,$lengthprev" >> timediff.csv
lengthprev=$length
time1=$time2

fi
#echo $hourinsec
#echo $seconds
#echo "$hour"
done
#cat $INPUT1 | awk -F' ' '{print $1 "," $NF}' > $OUTPUT1
#cat $INPUT1 > $OUTPUT1
