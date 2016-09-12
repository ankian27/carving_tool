#!/usr/bin/python
import re
import fileinput
import sys

stat_ok=re.compile('^HTTP/1.1\s\d\d\d\s')
stno=re.compile('\d{3}')
crlf=re.compile('\r\n')

cont_type=re.compile('Content-Type:')

cont_len=re.compile('Content-Length: ')

text_html=re.compile('text/html')

with open(sys.argv[1], 'rb') as f:

   while 1:
      line_in=f.readline()
      
      if not line_in: break   	

      pat = cont_type.search(line_in)
      if pat:
      	pat4=text_html.search(line_in)

        if pat4: # If it is text/html
           
        #pat1=stno.search(line)
          print pat4.group(0)
#  a="file_"+str(i)+".html"
 # print a
