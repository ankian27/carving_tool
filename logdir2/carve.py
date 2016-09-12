#!/usr/bin/python
import re
import fileinput
import sys


#^[0-9a-fA-F]{3}$


#for x in range(10):
#	print x
#i = int(s, 16)

#This is compilation of some of the patterns to be used frequently
get=re.compile('^GET')

stat_ok=re.compile('^HTTP/1.1 200 OK')

stat=re.compile('^HTTP/1.1\s\d\d\d\s')

stno=re.compile('\d{3}')

connection=re.compile('^Connection:')

crlf=re.compile('^\r\n$')

hexbytes=re.compile('^[0-9a-fA-F]{1,3}\s$')

cont_type=re.compile('Content-Type: ')

cont_len=re.compile('Content-Length: ')

text_html=re.compile('text/html')

image=re.compile('image')

length=re.compile('[0-9]*')
with open(sys.argv[1], 'rb') as f:
    #for line in f:
    while 1:
      line_in=f.readline()
      
      if not line2: break
      #search for GET pattern
      pat=get.search(line2)
      if pat:  #If the statement is GET
      	while 1:
      		line_status=f.readline()
      		
      		if not line_status: break

            pat2=stat.search(line_status)
            if pat2: #If it is the status line
               #line_type=f.readline()
               pat_statno=stno.search(statline_status)


               if pat_statno.group(0)==200:
                 while 1: #looking for the Content-Type
               	    line_type=f.readline()

               	    if not line_type: break

               	    pat3=cont_type.search(line_type)

               	    if pat3: #If it is the content-type line
               	    
               	      #line_form=f.read()
               	    
               	      pat4=text_html.search(line_type)# true if it is a text/html type

               	      pat_image=image.search(line_type)# true if it is image type

                      if pat4: # If it is text/html
               	  	    line_hex=f.readline()
               	  	    pat5=crlf.search(line_hex)

               	  	    while not pat5: #search till it finds the first carriage return
               	  	
                          line_hex=f.readline()
               	  	      if not line_hex: break

               	  	      pat5=crlf.search(line_hex)
               	  	  
               	  	      #if pat5:
                        line_hex=f.readline() # This is where it gets the first hex bytes string
                        pat_hexno=hexbytes.search(line_hex)

               	  	    i=int(pat_hexno.group(0),16)

               	  	    while i != 0: #read until it says 0
               	  		    body=f.read(i)
               	  		    """Output the body to a file"""

               	  		    line_hex==f.readline()
               	  		    pat5=hexbytes.search(line_hex)
               	  		    if pat5:
               	  		 	    i=int(pat5.group(0),16)
               	  		    else:
               	  			    break # breaking from counting because the required bytes have been read
               	  	    break 		#the text has been read so breaking from the content-type search

               	  
               	      elif  :
               	  	    """The code if it is image"""
               	  	    break # we will have a break at the end of this else too
                 break # breaking from looking for 200 OK status(already found the 200 OK status successfully)  	  	
            

               else:
                 break # If the status is not 200 OK break and look for the next GET




        #q1 In case of text/html what do we have to print to output file
        #q2 same with the image file
        #q3 other statuses for else

        #edits -
        #1 change status conditions-->done
        #2 change the hexbytes condition, we need the first hex no. after a newline/carriage return
        #3 Javascript too. so read the 'application' part and then the extension would be after the '/' sign
        #4 For image/XXX thing read the part after the / to the newline, that would be the extension

