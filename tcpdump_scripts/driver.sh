#!/bin/bash

#This is capturing traffic for 60 secs. 
tshark -i wlan0 -a duration:20 -t e -f tcp -w tr_dump.pcap #&& tcpdump -i wlan0 -G 15 -W 1 -w myfile.pcap


tshark -r tr_dump.pcap -T fields -e frame.time -e frame.len -t e -E separator=, > time_len.csv

#removing the year and date columns and making a new csv file with them
INPUT=time_len.csv

while IFS='' read -r line || [[ -n "$line" ]]; do
  
    length=$(echo $line | awk -F',' '{print $3}')

temp1=$(echo $line | grep -o -e "[0-9][0-9]:[0-9][0-9]:[0-9][0-9]\.[0-9]\{6\}") #[0-9][0-9][0-9][0-9][0-9]" )

echo "$temp1,$length" >> time_len2.csv

done < "$INPUT"
#done making the csv file

#making timediff vs len csv file
source ./timediff.sh

#making the plot for timediff vs len and time vs len
Rscript ./plots.r

tcptrace -l tr_dump.pcap >> stats.txt

#we can still add a few tcptrace graphs too

#after running the tcptrace for the graphs do the following


#mkdir plots
#mv *.xpl ./plots

#xplot.org *.xpl







