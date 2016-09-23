#!/usr/bin/Rscript


pack <- read.csv("timediff.csv", header=TRUE)

#print(pack$length)
diff <- pack$timediff
len <- pack$length
dev.new()  
plot(len,diff,xlim= c(0,1000),ylim = c(0,10000),main="time difference vs length")
#x11(plot(len,diff,xlim= c(0,1000),ylim = c(0,10000)))
dev.new()
plot(len,diff,xlim= c(0,4000),ylim = c(0,20000))


