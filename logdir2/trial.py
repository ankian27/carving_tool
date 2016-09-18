#!/usr/bin/python
import re
import fileinput
import sys

stat_ok=re.compile('^HTTP/1.1\s\d\d\d\s')
stno=re.compile('\d{3}')
crlf=re.compile('\r\n')
hexbytes=re.compile('^[0-9a-fA-F]{1,3}\s$')
cont_type=re.compile('Content-Type:')

cont_len=re.compile('Content-Length: ')

text_html=re.compile('text/html')
image_ext=re.compile('\w+\s')
leng=re.compile('[0-9]+')
length=re.compile('[0-9]+')
with open(sys.argv[1], 'rb') as f:

   while 1:
      line_in=f.readline()
      
      if not line_in: break   	

      pat = hexbytes.search(line_in)
      if pat:
      	str=pat.group(0)
      	str2=str[:-1]
      	i=int(str2,16)
      	ll=f.read(i)
      	if i!=0:
      	  print ll
      	new=f.readline()
      	#mew2=f.readline()
      	print i
      	#print new
      	#print mew2
      #pat=True
      #print pat
      #if pat:
      	#ext="."+pat.group(0)
      #	pat2=image_ext.search(line_in)
      #	stri=pat2.group(0)
      #	stri=stri[:-1]
      #	print stri

      #pat2=length.search(line_in)
      #	i=int(pat2.group(0))
      #	blank_line=f.readline()
      #	rrr=f.read(7)
      #	rest=f.readline()"""

      	#print rest,
        #if pat4: # If it is text/html
           
        #pat1=stno.search(line)
         # print pat4.group(0)
#  a="file_"+str(i)+".html"
 # print a
