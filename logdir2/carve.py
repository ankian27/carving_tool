#!/usr/bin/python
import re
import fileinput
import sys


#^[0-9a-fA-F]{3}$


#for x in range(10):
#	print x
#i = int(s, 16)

#This is compilation of some of the patterns to be used frequently
get=re.compile('(^GET|GET .* HTTP/1.[01])')

stat_ok=re.compile('^HTTP/1.1 200 OK')

stat=re.compile('^HTTP/1.1\s\d\d\d\s')

stno=re.compile('\d{3}')

connection=re.compile('^Connection:')

crlf=re.compile('^\r\n$')

hexbytes=re.compile('^[0-9a-fA-F]{1,10}\s$')

cont_type=re.compile('Content-Type: ')

cont_len=re.compile('Content-Length: ')

trans_enc=re.compile('Transfer-Encoding: chunked')

text_html=re.compile('text/html')

image=re.compile('image')

image_ext=re.compile('\w+\s')

leng=re.compile('\d+')

appl_js=re.compile('application/x-javascript')

appl_json=re.compile('application/json')

get_flag=0

rev_flag=0

rev_flag_json=0

file_count=1

with open(sys.argv[1], 'rb') as f:
    #for line in f:
   while 1:
      if get_flag==0: 
        line_in=f.readline()
      
        if not line_in: break
        #search for GET pattern
        pat=get.search(line_in)
      elif get_flag==1:
        pat=True
       
      if pat:  #If the statement is GET
        print "Get statement"
      	while 1:
      	    line_status=f.readline()
      		
      	    if not line_status: break

            pat2=stat.search(line_status)
            if pat2: #If it is the status line
               print "status line"
               #line_type=f.readline()
               pat_statno=stno.search(line_status)
               stano=int(pat_statno.group(0))

               if stano==200:
                 print "status 200"
                 while 1: #looking for the Content-Type
               	    line_type=f.readline()

               	    if not line_type: break

               	    pat3=cont_type.search(line_type)

               	    if pat3: #If it is the content-type line
               	    
               	      #line_form=f.read()
                      print "content-type"  
               	      pat4=text_html.search(line_type)# true if it is a text/html type

               	      pat_image=image.search(line_type)# true if it is image type

                      if pat4: # If it is text/html
                        
                            get_flag=0
               	  	    line_hex=f.readline()
               	  	    pat5=crlf.search(line_hex)
               	  	    filename="extract/"+"outfile"+ str(file_count) +".html"
               	  	    file=open(filename,'w')

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
               	  		    #Output the body to a file
                                    file.write(body)
               	  		    eol=f.readline()# This would read the CRLF at the end of the given no. of bytes so next readline would actually be the hex no.
                                    line_hex=f.readline()
               	  		    pat5=hexbytes.search(line_hex)
               	  		    if pat5:
               	  		 	    i=int(pat5.group(0),16)
               	  		    else:
               	  			    break # breaking from counting because the required bytes have been read
                            file.close()
                            file_count =file_count+1


               	  	    break 		#the text has been read so breaking from the content-type search

               	  
               	      elif pat_image:  #If it is an image.
                        print "image found"
                        pat6=image_ext.search(line_type)
                        temp=pat6.group(0)
                        ext=temp[:-1]
                        extension="." + ext  # Extract the image extension and save it
                        filename="extract/"+"image_outfile"+str(file_count)+extension
                        file=open(filename,'w')
                        while 1:
                          

                          line_len=f.readline()
                          if not line_len: break

                          pat7=cont_len.search(line_len) # Finding the "Content-length: " line

                          if pat7:
                            pat8=leng.search(line_len)

                            no_bytes=int(pat8.group(0))
                            #blank_line=f.readline() # reding the blankline after the "Content-length: " line
                            blank_line=f.readline()
                            pat5=crlf.search(blank_line)

                            while not pat5 :
                              blank_line=f.readline()
                              
                              if not blank_line: break
                              print blank_line,
                              pat5=crlf.search(blank_line)
                            #f.readline()   
                            image_content=f.read(no_bytes)   
                            file.write(image_content)
                            file.close()
                            file_count =file_count+1
                            next_get=f.readline()
                            pat9=get.search(next_get)
                            if pat9:
                              get_flag=1
                            else:
                              get_flag=0                          
                       

               	  	        
                            break # we will have a break at the end of this else too
                        break#the text has been read so breaking from the content-type search

                      else:
                        pat10=appl_js.search(line_type)

                        pat11=appl_json.search(line_type)

                        if pat10:
                          print "javascript" 
                          line_hex=f.readline()
                          pat5=crlf.search(line_hex)
                          filename="extract/"+"outfile"+str(file_count)+".txt"
                          file=open(filename,'w')
                          while not pat5: #search till it finds the first carriage return
                    
                            line_hex=f.readline()
                            if not line_hex: break
                            pat_len=cont_len.search(line_hex)
                            if pat_len:
                              rev_flag=1
                              pat8=leng.search(line_hex)
                              no_bytes=int(pat8.group(0))                             
                              
                            pat5=crlf.search(line_hex)
                          
                            #if pat5:
                          if rev_flag==0:
                            line_hex=f.readline() # This is where it gets the first hex bytes string
                          

                            pat_hexno=hexbytes.search(line_hex)

                            i=int(pat_hexno.group(0),16)

                            while i != 0: #read until it says 0
                              body=f.read(i)
                              """Output the body to a file"""
                              file.write(body)
                              eol=f.readline()# This would read the CRLF at the end of the given no. of bytes so next readline would actually be the hex no.
                              line_hex=f.readline()
                              pat5=hexbytes.search(line_hex)
                              if pat5:
                                i=int(pat5.group(0),16)
                              else:
                                break # breaking from counting because the required bytes have been read

                          elif rev_flag==1:
                             js_content=f.read(no_bytes)
                             file.write(js_content)
                             rev_flag=0

                          file.close()
                          file_count =file_count+1
                          break#the text has been read so breaking from the content-type search
                        elif pat11:
                            filename="extract/"+"outfile"+str(file_count)+".txt"
                            file=open(filename,'w')                        
                            while 1:
                          

                              line_len=f.readline()
                              if not line_len: break

                              pat7=cont_len.search(line_len) # Finding the "Content-length: " line
                              pat_encode=trans_enc.search(line_len)

                              if pat7:
                                pat8=leng.search(line_len)

                                no_bytes=int(pat8.group(0))
                                blank_line=f.readline() # reading the blankline after the "Content-length: " line 
                                image_content=f.read(no_bytes)   
                                file.write(image_content)
                                file.close()
                                file_count =file_count+1
                                next_get=f.readline()
                                pat9=get.search(next_get)
                                if pat9:
                                  get_flag=1
                                else:
                                  get_flag=0 

                                break

                              elif pat_encode:
                                pat5=crlf.search(line_len)
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
               	  		    #Output the body to a file
                                    file.write(body)
               	  		    eol=f.readline()# This would read the CRLF at the end of the given no. of bytes so next readline would actually be the hex no.
                                    line_hex=f.readline()
               	  		    pat5=hexbytes.search(line_hex)
               	  		    if pat5:
               	  		 	    i=int(pat5.group(0),16)
               	  		    else:
               	  			    break # breaking from counting because the required bytes have been read
                                file.close()
                                file_count =file_count+1                                
                                break 
                            break#the text has been read so breaking from the content-type search                        
                        else:
                          print "Error:Unknown Content-Type"      
                        break     #the text has been read so breaking from the content-type search                                                  

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

